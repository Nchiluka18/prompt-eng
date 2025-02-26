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

- Analyzing the impact of prompt variations on the accuracy and consistency of AI-generated financial recommendations.

- Comparing model responses with different parameter configurations (temperature, context window, number of predictions).

**Implications for practice**

- Enhancing the reliability of AI-driven financial planning tools.

- Automating requirement analysis for financial advisory services using optimized prompt structures.

- Identifying the best-performing prompt engineering techniques for real-world financial applications.

# Research Method

Experiment Setup

- We implemented the following prompt engineering techniques to analyze their effectiveness in financial planning:

- Zero-Shot Prompting – AI directly responds to financial queries without additional context.

- Few-Shot Prompting – Provides examples to guide AI in generating responses.

- Chain-of-Thought Prompting – Encourages step-by-step reasoning before arriving at a final recommendation.

- Self-Consistency Prompting – AI generates multiple responses and selects the most consistent one.

- Meta-Prompting – AI reflects on its reasoning process and iterates to refine financial strategies.

**Model Parameters and Variations**

The following parameters were tested across all prompting techniques:

1. Model: Qwen2

3. Temperature: 0.7 - 1.0 (higher values for diverse responses, lower for consistency)

5. Context Window (num_ctx): 100 - 200 tokens

7. Number of Predictions: 50 - 100 tokens

# Results

Describe the results achieved through your research process.

| Technique  | Strengths  | Observations & Considerations  | Avg Response Time(s)  |
| ------------ | ------------ | ------------ | ------------ |
| Zero-Shot  | Fast response, minimal setup  |May lack context, leading to generic answers   |  0.8 - 1.2 |
|  Few-Shot |More accurate, guided responses   |  Relies on well-curated examples for effectiveness |  1.5 - 2.0 |
| Chain-of-Thought  | Improved reasoning, better recommendations  | More thoughtful responses but takes longer  |   2.2 - 3.0|
|  Self-Consistency | Most reliable responses  | Generates multiple answers to ensure accuracy, but is resource-intensive  |  3.5 - 4.5 |
| Meta-Prompting  | Adaptive and optimized strategies  | Requires iterative refinement, but improves adaptability  |  4.0 - 5.5 |

**Key Observations**

- Few-Shot and Chain-of-Thought prompting performed well in structured financial planning scenarios.

- Self-Consistency produced the most reliable responses but required more computational resources.

- Meta-Prompting improved reasoning over iterations, making it ideal for complex financial queries.

# Further research

1. Investigating automated prompt generation using LLMs.

3. Enhancing AI’s ability to personalize financial advice based on user-specific goals.

5. Exploring hybrid approaches that combine multiple prompt techniques for optimal performance.

This research provides valuable insights into prompt engineering for financial advisory services, offering a roadmap for further innovation in AI-driven financial planning.
