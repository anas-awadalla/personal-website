import random

from transformers import AutoTokenizer, T5ForConditionalGeneration


def scratchpad(st):
    st.header(
        "Show Your Work: Scratchpads for Intermediate Computation with Language Models")
    st.subheader("Overview")

    st.markdown(
        """
        In this post I will explore the idea of explicitly prompting language models to perform intermediate computations to improve performance on math tasks.
        This line of work is interesting as it debunks the idea that language models are only good at generating text, and instead shows that they can be used to perform computations 
        but need to be prompted in specific ways.
        """
    )

    st.subheader("Technical Notes")
    st.markdown(
        """
        I will be using the [Flan T5 Small](https://huggingface.co/google/flan-t5-small) model for this demo and the [Show Your Work](https://arxiv.org/abs/2112.00114) paper as a guide for how to prompt the model.
        We will explore how the model performs on basic arithmetic tasks using both direct prompting and scratchpad methods. The whole idea behind scratchpads
        is to allow the model to output intermediate computations and therefore increase its likelihood of getting the final answer correct.
        """
    )

    def generate_step(prompt, max_tokens=2, min_tokens=1):
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = T5ForConditionalGeneration.from_pretrained(
            "google/flan-t5-small")
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        output = model.generate(input_ids, max_new_tokens=max_tokens, min_length=min_tokens)
        output = tokenizer.decode(output[0], skip_special_tokens=True)
        output = output.split("=")[-1]
        output = output.split("+")[-1]
        return output.strip()

    def split_num_into_digits(num):
        return " ".join([digit for digit in str(num)])

    st.subheader("Trying out the paper's ideas")
    st.markdown(
        """
        Let's start with some basic arithmetic. 
        """
    )

    num_1 = random.randint(0, 5)
    num_2 = random.randint(0, 5)
    correct_answer = num_1 + num_2
    text = st.text_input("A simple arithmetic problem (e.g. 1 + 1)",
                         f"{split_num_into_digits(num_1)} + {split_num_into_digits(num_2)}")

    st.write("Let's see how the model performs on this task.")
    if st.button("Try Direct Prompting!"):
        generated_answer = generate_step(f"Input: {text}\nTarget:")
        if generated_answer == "":
            st.error("Model output nothing! Try again.")
        else:

            try:
                if int(generated_answer) == correct_answer:
                    st.success(
                        f"Model output **{generated_answer}** and is correct!")
                else:
                    st.error(
                        f"Model output **{generated_answer}** but answer is **{correct_answer}**")
            except:
                st.error("Model output something that is not a number! Try again.")

    st.markdown(
        """
        **Ok so the model struggles with this task. Let's see if few-shot prompting can help.**
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        fewshot_btn = st.button("Try Few-Shot Direct Prompting!")
    with col2:
        num_shots = st.number_input(
            "Number of shots", min_value=1, max_value=16, value=4, step=1)

    if fewshot_btn:
        # generate a few samples and out put to the user
        demonstrations = []
        for _ in range(num_shots):
            demo_num_1 = random.randint(0, 5)
            demo_num_2 = random.randint(0, 5)
            demo_answer = demo_num_1 + demo_num_2
            demo_text = f"Input: {split_num_into_digits(demo_num_1)} + {split_num_into_digits(demo_num_2)}\nTarget: {split_num_into_digits(demo_answer)}"
            demonstrations.append(demo_text)
        demonstrations = "\n".join(demonstrations)
        st.text_area("Demonstrations we will use to prompt the model",
                     demonstrations, height=100)

        generated_answer = generate_step(
            f"{demonstrations}\nInput:{text}\nTarget: ")
        if generated_answer == "":
            st.error("Model output nothing! Try again.")
        else:
            if int(generated_answer) == correct_answer:
                st.success(
                    f"Model output **{generated_answer}** and is correct!")
            else:
                st.error(
                    f"Model output **{generated_answer}** but answer is **{correct_answer}**")

    st.markdown(
        """
        **You will find that the model seems to output the wrong answer at times despite being prompted with many examples. Let's see if scratchpads solve this!**
        """
    )
    st.markdown(
        """
        I will use the scratchpad demonstration from the paper as these are hard to generate on the fly. 
        The scratchpad demonstration is as follows:
    
        ```
        Input: 2 9 + 5 7
        Target:
        <scratch>
        2 9 + 5 7 , C : 0
        2 + 5 , 6 C : 1 # added 9 + 7= 6 carry 1 
        , 8 6 C: 0 #added 2 + 5 + 1 = 8 carry 0
        0 8 6
        </scratch>
        8 6
        ```
        
        """
    )

    scratchpad_demonstration = "Input: 2 9 + 5 7\nTarget:\n<scratch>\n2 9 + 5 7 , C : 0\n2 + 5 , 6 C : 1 # added 9 + 7= 6 carry 1 \n, 8 6 C: 0 #added 2 + 5 + 1 = 8 carry 0\n0 8 6\n</scratch>\n8 6"
    scratchpad_btn = st.button("Try Scratchpad Prompting!")
    if scratchpad_btn:
        generated_answer = generate_step(
            f"{scratchpad_demonstration}\nInput:\n{text}\nTarget:\n<scratch>\n", min_tokens=30, max_tokens=30)
        generated_answer = generated_answer.split(
            "</scratch>")[-1].split(
            "Target")[0].replace(" ", "").strip()
        
        if generated_answer == "":
            st.error("Model output nothing! Try again.")
        else:
            try:
                if int(generated_answer) == correct_answer:
                    st.success(
                        f"Model output **{generated_answer}** and is correct!")
                else:
                    st.error(
                        f"Model output **{generated_answer}** but answer is **{correct_answer}**")
            except:
                st.error("Model output something that is not a number! Try again.")
                
    st.markdown(
        """
        You may find that despite using the scratchpad, the model still outputs the wrong answer. I hypothesize that this is because of the small model we are using to run these experiments. 
        The paper uses a much larger model and I believe that this is why the model is able to output the correct answer in the paper.
        """
    )
