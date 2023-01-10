from transformers import AutoTokenizer, T5ForConditionalGeneration

def lm_are_zeroshot_planners(st):
    st.header("Language Models Are Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents")
    st.write(
        """
        This is the first of a series of blog posts for the [CSE 599](https://cse599d1wi23.notion.site/cse599d1wi23/CSE-599-D1-Winter-2023-fe73cb56c11b45efb34e94c090480791) course I am taking. 
        For each of these posts I will be explaining a paper and implementing some of the ideas in it.
        For this post I will be writing about [Language Models Are Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents](https://arxiv.org/abs/2201.07207).       
        """
    )
    st.subheader("Overview")
    st.write(
        """
        This paper proposes using LLMs to dissect high level goals into actionable steps. The authors show that without any additional training a pre-training LLMs can 
        be prompted to generate a sequence of actions that can be used to achieve a given goal and show that this can be used to control an embodied agent.
        """
    )
    st.subheader("Technical Notes")
    st.markdown("""
    ##### Task
    Given a list of possible actions and a target task, the goal is to compose step by step actions that can be used to achieve the target task. 

    ###### Evaluation Metrics
    The authors evaluate their method using the following metrics:
    - **Executability**: This measures weather a procedure is executable, even if it is incorrect, within the confines of the simulation.
    - **Correctness**: This is a metric that assess weather human annotators believe the procedure is correct.

    ##### Modeling
    The first part of the modeling pipeline is a **Planning LM**:
    - The authors used pre-trained LLMs to compose generation steps.\\
    - They achieved best results when using GPT-3 and Codex.\\
    - Interestingly a 12B code LM outperforms a 13B GPT-3 model which maybe alludes to how the structure of code text can improve performance.
    
    The second part of the modeling pipeline is a **Translation LM**:
        - This is a model used to embed all the possible actions as well as each generated step.\\
        - The each generated step is then mapped to one of the possible actions based on cosine distance.\\
        - This is done after generating each individual step and the mapped action is concatenated to the prompt for the next generation.

    ##### Prompting
    - The authors prompted the **Planning LM** with a single example that is similar to the query action.
    - The prompt is formatted as follows:
        ```
        Task: <target task>
        Step 1: <step 1>
        ....
        ```
    - For each step the authors sampled multiple potential generations and used the **translation LM** to find the one with highest similarity to an environment action.
    """)
    actions = """gather ingredients, preheat oven, grease and flour pan, sift dry ingredients, cream butter and sugar, beat in eggs, stir in vanilla, alternate adding dry ingredients and milk, pour batter into pan, tap pan gently, place in oven, bake according to recipe, test for doneness, remove from oven, cool in pan, turn out onto wire rack, make frosting or glaze, mix sugar and butter, beat in vanilla and milk, beat frosting until smooth, spread frosting over cake, decorate with sprinkles, cut and serve, store leftovers, refrigerate if necessary, heat slice in microwave, enjoy, make simple syrup, boil sugar and water, brush over cooled layers, make chocolate ganache, chop chocolate, heat cream, pour over chocolate, whisk until smooth, cool and thicken, frost cake, make meringue frosting, beat egg whites and sugar, add vanilla, frost cake, make fruit filling or topping, wash and prepare fruit, cut into pieces, mix with sugar and cornstarch, spread over cake layer, top with fresh fruit, make whipped cream frosting, beat heavy cream, add sugar and vanilla, beat until stiff peaks form"""
    st.subheader("Trying out the paper's ideas")
    st.write(
        """
        Now that we have the technical details out of the way, I want to demo how this might work with a smaller language model. I will be using the [Flan T5 Small](https://huggingface.co/google/flan-t5-small) model.
        """
    )
    st.write(
        """
        Imagine we are trying to generate steps for making a cake.

        We will use a single in-context example and format the prompt as follows:          
        """
    )

    prompt = st.text_area("Prompt", height=180, value="""Task: Make a coffee\nStep 1: Grab a coffee mug\nStep 2: Get coffee beans\nStep 3: Brew coffee using a machine\n\nTask: Make a cake\nStep 1:""")

    st.write(
        """
        The next step is to generate the first step for making a cake. In the paper the authors sampled multiple potential completions. For the sake of compute I will just sample a single output.
        """
    )

    def generate_step(prompt):
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        output = model.generate(input_ids, max_length=25, do_sample=True, num_return_sequences=1, temperature=0.7)
        output = tokenizer.decode(output[0], skip_special_tokens=True)
        return output

    if st.button("Generate Step 1", type="primary"):
        step_1 = generate_step(prompt=prompt).replace(".", "")
        st.session_state['step_1'] = step_1
        if 'fix_step_1' in st.session_state:
            del st.session_state['fix_step_1']
        st.success("Step 1: " + step_1, icon="🎂")
    
    if 'step_1' in st.session_state and 'fix_step_1' not in st.session_state:
        st.write(
            """
            Now that we have our generated step we need to map it to a valid action. Ideally this would be using a **translator LM** like BERT to find the most similar environment action. However, **to avoid bloating my website I will choose the action with the most overlapping words to the generated text**.
            """
        )
        closest_action = max(actions.split(", "), key=lambda x: len(set(x.split(" ")).intersection(set(st.session_state['step_1'].split(" ")))))
        st.session_state['fix_step_1'] = True
        st.markdown(f"We end up mapping :orange[{st.session_state['step_1']}] to :green[{closest_action}] and will use this for the rest of the generation steps.")
        st.session_state['step_1'] = closest_action


    if 'step_1' in st.session_state and 'fix_step_1' in st.session_state:
        if st.button("Generate Step 2", type="primary"):
            step_2 = generate_step(prompt=prompt+st.session_state['step_1']+"\n").replace(".", "")
            st.session_state['step_2'] = step_2
            closest_action = max(actions.split(", "), key=lambda x: len(set(x.split(" ")).intersection(set(step_2.split(" ")))))
            st.session_state['fix_step_2'] = True
            st.session_state['step_2'] = closest_action
            st.success(f"Step 2 is :orange[{step_2}] but is mapped to **{closest_action}**", icon="🍰")

    
    if 'step_2' in st.session_state and 'fix_step_2' in st.session_state:
        if st.button("Generate Step 3", type="primary"):
            step_3 = generate_step(prompt=prompt+st.session_state['step_1']+"\n"+st.session_state['step_2']+"\n").replace(".", "")
            closest_action = max(actions.split(", "), key=lambda x: len(set(x.split(" ")).intersection(set(step_3.split(" ")))))
            st.session_state['fix_step_3'] = True
            st.session_state['step_3'] = closest_action
            st.success(f"Step 3 is :orange[{step_3}] but is mapped to **{closest_action}**", icon="🥮")

    if 'step_3' in st.session_state:
        st.write(
            """
            We could go on but you get the point! The generations are not bad for a very small language model. As expected scale should drastically helps. You can now clear the session using the button below and go back and play with the prompt and generate output for different tasks 🥳.
            """
        )

    st.write("")
    st.write("")
    st.write("")
    if st.button("Clear session (do this at the start of each generation)", type="secondary"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
