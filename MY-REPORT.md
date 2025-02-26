![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# Exploring Prompt Engineering Techniques for Automated Financial Planning


This research explores various prompt engineering techniques to optimize automated financial planning, enhancing the accuracy and efficiency of AI-driven financial advisory services.


* Authors: Neha Chiluka(jchiluka2024@fau.edu), Tejaswini Porachenu(tporachenu2024@fau.edu), Shivani Vilambi(svilambi2024@fau.edu). 
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

  
# Research Question 

How can different prompt engineering techniques improve the accuracy and efficiency of AI-driven financial advisory services?

## Arguments

**What is already known about this topic**

- Large language models (LLMs) can assist in financial planning by analyzing income, expenses, and investment options.

- Prompt engineering can significantly improve AI responses by structuring input in various ways.

- Techniques such as zero-shot, few-shot, chain-of-thought, meta-prompting, and self-consistency have shown promise in different domains.

**What this research is exploring**

- Experimenting with different prompt engineering techniques for financial advisory applications.

- Testing different prompt templates for requirement analysis to improve accuracy.

- Exploring automated prompt generation and its impact on AI-driven financial planning.

- Experimenting with a combination of prompt engineering techniques, automated prompt generation, and model parameter variations to optimize both latency and accuracy.

- Evaluating the effectiveness of scenario-based prompt selection to enhance AI-driven financial advisory services.

**Implications for practice**

- Enhancing the reliability of AI-driven financial planning tools.

- Automating requirement analysis for financial advisory services using optimized prompt structures.

- Identifying the best-performing prompt engineering techniques for real-world financial applications.

- Understanding the trade-offs between different prompt engineering techniques in terms of performance, accuracy, and computational efficiency.

# Research Method

Experiment Setup

We implemented the following prompt engineering techniques to analyze their effectiveness in financial planning:

- **Zero-Shot Prompting** – AI directly responds to financial queries without additional context.

- **Few-Shot Prompting** – Provides examples to guide AI in generating responses.

- **Chain-of-Thought Prompting** – Encourages step-by-step reasoning before arriving at a final recommendation.

- **Self-Consistency Prompting** – AI generates multiple responses and selects the most consistent one.

- **Meta-Prompting** – AI reflects on its reasoning process and iterates to refine financial strategies.

- **Automated Prompt Generation** – AI dynamically generates prompts based on input data to optimize response quality.


**Model Parameters and Variations**

We tested multiple models to compare their effectiveness across different prompting techniques:

- **Models:** Qwen2, Phi-4, LLaVA (via Open-WebUI)

- **Temperature:** 0.5 - 1.0 (higher values for diverse responses, lower for consistency)

- **Context Window (num_ctx):** 100 - 300 tokens

- **Number of Predictions:** 50 - 150 tokens

- **Automated Prompting:** Enabled for selected experiments

**Example Prompts for Financial Planning Scenarios**

**Budgeting Advice:**

"You are a financial advisor. A client earns $5000 monthly and has expenses of $3200. They want to save $10,000 in 12 months. Provide a financial strategy focusing on budgeting and savings."

**Investment Strategy:**

"A client has a $20,000 investment budget and is looking for low-risk options. Suggest an optimal investment portfolio based on current market conditions."

**Debt Management:**

"A client has a $15,000 credit card debt with a 15% interest rate. Recommend a repayment strategy while balancing other financial obligations."
# Results

Comparison of Prompting Techniques Across Models.

| Technique  | Strengths  | Observations & Considerations  | Avg Response Time (s) (Qwen2 / Phi-4 / LLaVA)  |
| ------------ | ------------ | ------------ | ------------ |
| Zero-Shot  | Fast response, minimal setup  |May lack context, leading to generic answers   |  0.8 - 1.2 / 0.7 - 1.1 / 1.0 - 1.3 |
|  Few-Shot |More accurate, guided responses   |  Relies on well-curated examples for effectiveness |  1.5 - 2.0 / 1.4 - 1.8 / 1.8 - 2.3 |
| Chain-of-Thought  | Improved reasoning, better recommendations  | More thoughtful responses but takes longer  |   2.2 - 3.0 / 2.0 - 2.8 / 2.5 - 3.5|
|  Self-Consistency | Most reliable responses  | Generates multiple answers to ensure accuracy, but is resource-intensive  |  3.5 - 4.5 / 3.2 - 4.0 / 4.0 - 5.2|
| Meta-Prompting  | Adaptive and optimized strategies  | Requires iterative refinement, but improves adaptability  |  4.0 - 5.5 / 3.8 - 5.0 / 4.5 - 6.0 |
| Automated Prompting | Dynamically optimized prompts | Can lead to variable results depending on data input and model behavior  |  2.5 - 3.5 / 2.2 - 3.0 / 2.8 - 4.0 |


**Key Observations**

- Few-Shot and Chain-of-Thought prompting performed well in structured financial planning scenarios.

- Self-Consistency produced the most reliable responses but required more computational resources.

- Meta-Prompting improved reasoning over iterations, making it ideal for complex financial queries.

- **Automated Prompting showed promise but required further fine-tuning to ensure consistency across different scenarios.**

- Phi-4 demonstrated faster response times compared to Qwen2 and LLaVA, while LLaVA produced more detailed and structured outputs but at the cost of latency.



# Further research

- Investigating advanced automated prompt generation techniques for enhanced AI-driven financial planning.

- Exploring the combination of different prompt engineering methods to optimize both speed and accuracy.

- Improving personalization of AI-generated financial advice based on user-specific goals.

- Testing additional models beyond Qwen2, Phi-4, and LLaVA to benchmark performance across different architectures.

This research provides valuable insights into prompt engineering for financial advisory services, offering a roadmap for further innovation in AI-driven financial planning.


