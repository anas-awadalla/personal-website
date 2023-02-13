
import matplotlib.pyplot as plt
import torch
from tokenizers import ByteLevelBPETokenizer
from transformers import (GPT2Config, GPT2LMHeadModel, LineByLineTextDataset,
                          PreTrainedTokenizerFast)


def chinchilla(st):

    @st.experimental_singleton
    def init():
        # Initialize a tokenizer
        tokenizer = ByteLevelBPETokenizer()

        # Customize training
        tokenizer.train(files=["corpus.txt"], vocab_size=256, min_frequency=2, special_tokens=[
            "<s>",
            "</s>",
            "<unk>",
            "<mask>",
        ])

        config = GPT2Config(n_positions=32, n_embd=8, n_layer=1,
                            n_head=1, n_inner=8, vocab_size=256)
        pico_model = GPT2LMHeadModel(config)
        print(f"Number of parameters: {pico_model.num_parameters()}")

        config = GPT2Config(n_positions=32, n_embd=8, n_layer=4,
                            n_head=1, n_inner=8, vocab_size=256)
        nano_model = GPT2LMHeadModel(config)
        print(f"Number of parameters: {nano_model.num_parameters()}")

        config = GPT2Config(n_positions=32, n_embd=8, n_layer=8,
                            n_head=1, n_inner=8, vocab_size=256)
        micro_model = GPT2LMHeadModel(config)
        print(f"Number of parameters: {micro_model.num_parameters()}")

        # Load it using transformers
        tokenizer = PreTrainedTokenizerFast(
            tokenizer_file="byte-level-BPE.tokenizer.json")
        tokenizer.add_special_tokens({'pad_token': '<pad>'})

        # train the model
        dataset = LineByLineTextDataset(
            tokenizer=tokenizer,
            file_path="corpus.txt",
            block_size=32,
        )

        return pico_model, nano_model, micro_model, dataset

    pico_model, nano_model, micro_model, dataset = init()
    
    if "x" not in st.session_state:
        st.session_state["x"] = []
        st.session_state["pico_small_loss"] = []
        st.session_state["nano_small_loss"] = []
        st.session_state["micro_small_loss"] = []
        
    if "fig" not in st.session_state:
        st.session_state["fig"], st.session_state["ax"] = plt.subplots()

    @st.cache(show_spinner=False)
    def train(model, samples=10000):
        model.train()
        loss = 0
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
        for sample in dataset[:samples]:
            loss = model(sample["input_ids"], labels=sample["input_ids"])[0]
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

    @st.cache(show_spinner=False)
    def evaluate(model):
        model.eval()
        # evaluate the model on 30k samples
        avg_loss = 0
        for sample in dataset[30000:]:
            loss = model(sample["input_ids"], labels=sample["input_ids"])[0]
            avg_loss += loss.item()
        avg_loss = avg_loss / len(dataset[30000:])
        print(f"Average loss: {avg_loss}")
        return avg_loss

    st.header("Training Compute Optimal Models (Chinchilla)")
    st.write("In this post I will explore the tradeoff between model size and training data size by pre-training small GPT-2 variants on a small corpus of Shakespeare text. The findings of the Chinchilla paper are exciting because they show how we can train more compact models that perform comparably to larger models. This makes these models easier to deploy.")
    st.write("Here I aim to replicate the results of the Chinchilla paper by training a small GPT-2 model on a small corpus of Shakespeare text. My main contribution is to provide an end to end demo for how to run the scaling experiments yourself.")
    st.subheader("Model Size")
    st.write("Here I introduce 3 new GPT-2 variants. I chose these models to be unrealistically small to be able to quickly train them on a small corpus online.")
    st.write("The following table shows the number of parameters in each GPT-2 model we train.")
    st.write("**GPT-2 pico** 2,784 parameters")
    st.write("**GPT-2 nano** 6,336 parameters")
    st.write("**GPT-2 micro** 15,744 parameters")
    st.write("We train each model on a small corpus of Shakespeare text.")
    st.subheader("Results")
    st.write("*I am not sure yet if this replicates the results of the Chinchilla paper. I will update this post when I have more results and do more hyperparameter optimizations.*")
    st.write("The following graphs show the loss of each model as the number of samples used to train it increases.")

    st.write("To run the scaling experiments you can click on the \"Train\" button below. This will train the model on the number of samples specified and add a marker to the graph. You can train the model on more samples by clicking the button again. The graph will update with the new marker.")
    samples = [100, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
    plot_spot = st.empty()
    
    if st.button("Train", type="primary"):
        # remove old markers from graph
        for line in st.session_state["ax"].lines:
            line.remove()
        for marker in st.session_state["ax"].collections:
            marker.remove()
        num_samples = samples[len(st.session_state["x"])]
        fig, ax = st.session_state["fig"], st.session_state["ax"]
        ax.set_xlabel("Number of samples")
        ax.set_ylabel("Loss")

        st.session_state['x'].append(num_samples)
        
        st.write(f"Training on {num_samples} samples")
        init()
        train(micro_model, samples=num_samples)
        st.session_state["micro_small_loss"].append(evaluate(micro_model))
        ax.scatter(
        st.session_state['x'],
        st.session_state["micro_small_loss"], label="micro", color="red")
        ax.plot(
        st.session_state['x'], st.session_state["micro_small_loss"], label="micro", color="red")
        ax.legend()
        with plot_spot:
            st.pyplot(fig)

        train(nano_model, samples=num_samples)
        st.session_state["nano_small_loss"].append(evaluate(nano_model))
        ax.scatter(
        st.session_state['x'],
        st.session_state["nano_small_loss"], label="nano", color="green")
        ax.plot(st.session_state['x'],
            st.session_state["nano_small_loss"], label="nano", color="green")
        ax.legend()
        # replace the previous plot with the new one
        with plot_spot:
            st.pyplot(fig)

        train(pico_model, samples=num_samples)
        st.session_state["pico_small_loss"].append(evaluate(pico_model))
        ax.scatter(
        st.session_state['x'],
        st.session_state["pico_small_loss"], label="pico", color="blue")
        ax.plot(st.session_state['x'],
            st.session_state["pico_small_loss"], label="pico", color="blue")
        ax.legend()
        with plot_spot:
            st.pyplot(fig)
        

    # plot the loss of each model based on the number of samples used to train it

    if st.button("Reset"):
        st.session_state["x"] = []
        st.session_state["pico_small_loss"] = []
        st.session_state["nano_small_loss"] = []
        st.session_state["micro_small_loss"] = []
        st.session_state["fig"], st.session_state["ax"] = plt.subplots()
        init()
        
        # refresh the page
        st.experimental_rerun()