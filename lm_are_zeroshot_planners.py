from transformers import AutoTokenizer, T5ForConditionalGeneration

def lm_are_zeroshot_planners(st):
    st.header("Language Models Are Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents")
    st.write(
        """
        This is the first of a series of blog posts for the [CSE 599](https://cse599d1wi23.notion.site/cse599d1wi23/CSE-599-D1-Winter-2023-fe73cb56c11b45efb34e94c090480791) course I am taking. 
        For each of these posts I will be explaining a paper and impelmenting some of the ideas in it.
        For this post I will be writring about [Language Models Are Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents](https://arxiv.org/abs/2201.07207).       
        """
    )
    st.subheader("Overview")
    st.write(
        """
        This paper proposes using LLMs to dissect high level goals into actionable steps. The authors show that without any additional training a pre-training LLMs can 
        be prompted to generate a sequence of actions that can be used to achieve a given goal and show that this can be used to control an emodied agent.
        """
    )
    st.subheader("Technical Details")
    st.markdown("""
    ##### Task
    Given a list of possible actions and a target task, the goal is to compose step by step actions that can be used to achieve the target task. 

    ###### Evaluation Metrics
    The authors evaluate their method using the following metrics:
    - **Executability**: The percentage of tasks that the agent was able to complete.
    - **Correctness**: The percentage of tasks that the agent was able to complete.

    ##### Modeling


    ##### Prompting

    """)
    actions = """gather ingredients, preheat oven, grease and flour pan, sift dry ingredients, cream butter and sugar, beat in eggs, stir in vanilla, alternate adding dry ingredients and milk, pour batter into pan, tap pan gently, place in oven, bake according to recipe, test for doneness, remove from oven, cool in pan, turn out onto wire rack, make frosting or glaze, mix sugar and butter, beat in vanilla and milk, beat frosting until smooth, spread frosting over cake, decorate with sprinkles, cut and serve, store leftovers, refrigerate if necessary, heat slice in microwave, enjoy, make simple syrup, boil sugar and water, brush over cooled layers, make chocolate ganache, chop chocolate, heat cream, pour over chocolate, whisk until smooth, cool and thicken, frost cake, make meringue frosting, beat egg whites and sugar, add vanilla, frost cake, make fruit filling or topping, wash and prepare fruit, cut into pieces, mix with sugar and cornstarch, spread over cake layer, top with fresh fruit, make whipped cream frosting, beat heavy cream, add sugar and vanilla, beat until stiff peaks form"""
    st.subheader("Trying out the paper's ideas")
    st.write(
        """
        Now that we have the technical details out of the way, I want to demo how this might work with a smaller language model. I will be using the [Flan T5 Base](https://huggingface.co/google/flan-t5-base) model.
        """
    )
    st.write(
        """
        Imagine we are trying to generate steps for making breakfast.

        We will use a single in-context example and format the prompt as follows:          
        """
    )

    prompt = st.text_area("Prompt", height=180, value="""Task: Make a coffee\nStep 1: Grab a coffee mug\nStep 2: Get coffee beans\nStep 3: Brew coffee using a machine\n\nTask: Make a cake\nStep 1:""")

    st.write(
        """
        The next step is to generate a single step for making breakfast. In the paper the author's sampled multiple potential completions. For the sake of compute I will just sample a single output.
        """
    )

    def generate_step(prompt):
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        output = model.generate(input_ids, max_length=20, do_sample=True, num_return_sequences=1)
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
            Now that we have our generated step we need to map it to a valid action. Ideally this would be using another translator LM like BERT. However, to avoid bloating my website I will just choose the action with the most overlapping words to the generated step.
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

    if 'step_3' in st.session_state and 'fix_step_3' in st.session_state:
        if st.button("Generate Step 4", type="primary"):
            step_4 = generate_step(prompt=prompt+st.session_state['step_1']+"\n"+st.session_state['step_2']+"\n"+st.session_state['step_3']+"\n").replace(".", "")
            closest_action = max(actions.split(", "), key=lambda x: len(set(x.split(" ")).intersection(set(step_4.split(" ")))))
            st.session_state['fix_step_4'] = True
            st.session_state['step_4'] = closest_action
            st.success(f"Step 4 is :orange[{step_4}] but is mapped to **{closest_action}**", icon="😋")
    
    if 'step_3' in st.session_state:
        st.write(
            """
            We could go on but you get the point! You can now clear the session using the button below and go back and play with the prompt and generate output for different tasks 🥳.
            """
        )

    st.write("")
    st.write("")
    st.write("")
    if st.button("Clear session (do this at the start of each generation)", type="secondary"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
