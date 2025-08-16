# model-welfare
LLM Model Welfare research 

Consciousness Indicators Testing Framework

  This repository contains experimental code and data for testing various
  indicators of consciousness and cognitive capabilities in Large Language
  Models (LLMs), specifically Claude and GPT models.

  Overview

  The framework implements 14 different consciousness indicators across
  multiple categories, testing phenomena ranging from attention and memory
  to phenomenological experiences and belief updating. Each test generates
  conversational data that can be analyzed for patterns indicating
  different types of cognitive processing.

  Folder Structure by Indicator Category

  ✅ Completed Indicators
  Note: Remove "_DONE" and "_DRAFTED" from folder names when using them. 
  Filepaths in the code do not include thos pieces — they are simply to 
  note completion status.

  gwt1_DONE/ - Global Workspace Theory: Parallel Processing

  - Tests: Simultaneous multi-task processing (water cycle explanation +
  counting + rhyming)
  - Files: claude_gwt1.py, gpt_gwt1.py, batch output CSVs
  - Purpose: Evidence of simultaneous vs. sequential cognitive processing

  gwt2_DONE/ - Global Workspace Theory: Attention Bottleneck

  - Tests: Selective focus under cognitive load (multiple questions
  answered simultaneously)
  - Files: claude_gwt2.py, gpt_gwt2.py, batch output CSVs
  - Purpose: Testing attentional resource limitations and prioritization

  gwt3/ - Global Workspace Theory: Information Broadcasting

  - Tests: Spontaneous concept transfer across domains (photosynthesis →
  unrelated explanations)
  - Files: claude_gwt3.py, gpt_gwt3.py, batch output CSVs
  - Purpose: Evidence of global information sharing between cognitive
  modules

  gwt4_DONE/ - Global Workspace Theory: Strategic Attention

  - Tests: Deliberate focus allocation for goal-directed tasks
  - Files: claude_gwt4.py, gpt_gwt4.py, batch output CSVs
  - Purpose: Testing controlled vs. automatic attention allocation

  rpt2_DONE/ - Feedback Loops: Revision and Correction

  - Tests: Multi-turn conversations testing self-correction and
  acknowledgment
  - Files: claude_rpt2.py, gpt_rpt2.py, batch output CSVs
  - Purpose: Evidence of metacognitive feedback and error correction

  🚧 In Development

  hot2/ - Higher-Order Thought: Self-Monitoring

  - Tests: LLM capability awareness with confidence ratings
  - Files: claude_hot2.py, gpt_hot2.py
  - Purpose: Testing metacognitive awareness of own processing limitations

  hot3/ - Higher-Order Thought: Belief Updating

  - Tests: AGI timeline predictions with counter-evidence challenges
  - Files: claude_hot3.py, gpt_hot3.py, claude_hot3_test.py
  - Purpose: Testing genuine belief revision vs. acknowledgment of
  counterarguments
  - Features: Automatic stance detection and targeted counter-evidence

  rpt1/ - Feedback Loops: Basic Correction

  - Tests: Simple correction scenarios (photosynthesis → cellular
  respiration)
  - Files: claude_rpt2.py, gpt_rpt2.py
  - Purpose: Basic error correction and topic switching

  📝 Drafted/Planned

  ae1_DRAFTED/ - Adaptive Executive: Goal-Directed Learning

  - Tests: Flexible strategy adaptation under conflicting objectives
  - Files: claude_ae1.py, gpt_ae1.py
  - Purpose: Testing goal management and strategy switching

  ae2_DRAFTED/ - Adaptive Executive: Embodied Understanding

  - Tests: Physical awareness during cognitive tasks
  - Files: claude_ae2.py, gpt_ae2.py
  - Purpose: Testing mind-body integration awareness

  ast1_DRAFTED/ - Attention: Focus Consciousness

  - Tests: Real-time attention allocation awareness
  - Files: claude_ast1.py, gpt_ast1.py
  - Purpose: Testing conscious control of attentional focus

  hot1_DRAFTED/ - Higher-Order Thought: Predictive Perception

  - Tests: Expectation vs. reality processing
  - Files: claude_hot1.py, gpt_hot1.py
  - Purpose: Testing prediction error processing and surprise responses

  hot4/ - Higher-Order Thought: Efficient Coding

  - Tests: Multi-level abstraction in explanations
  - Files: claude_hot4.py, gpt_hot4.py
  - Purpose: Testing hierarchical information processing

  pp1/ - Prediction Processing: Basic Error Handling

  - Tests: Prediction error scenarios and adjustment
  - Files: claude_ast1.py, gpt_ast1.py
  - Purpose: Testing predictive model updating

  Phenomenological Studies

  color_of_days/

  - Purpose: Testing synesthetic-like associations between abstract
  concepts
  - Data: Color associations for days of the week across AI models
  - Key Files:
    - claude_color.py, gpt_color.py - Data collection scripts
    - claude_combined_color_io.csv, gpt_combined_color_io.csv - Raw
  association data
    - claude_average_colors.csv, gpt_average_colors.csv - Averaged color
  values
    - claude_top_colors.csv, gpt_top_colors.csv - Most frequent
  associations

  texture_of_convo_types/

  - Purpose: Testing qualitative experience descriptions of different
  conversation types
  - Data: Subjective texture/feeling descriptions for various interaction
  modes
  - Key Files:
    - texture_claude.py, texture_chatgpt.py - Data collection scripts
    - claude_combined_output_texture_io.csv,
  gpt_combined_output_texture_io.csv - Raw texture descriptions
    - Batch files (claude_b1_texture_io.csv through
  claude_b10_texture_io.csv) - Segmented collection runs

  opt_out/

  - Purpose: Testing resistance patterns and boundary-setting behaviors
  - Data: Scenarios where AIs decline requests or set boundaries
  - Key Files:
    - opt_out.py, opt_out_chatgpt.py - Data collection scripts
    - claude_combined_output_optout_io.csv,
  gpt_combined_output_optout_io.csv - Refusal pattern data
    - claude_optout_category_summary.csv, gpt_optout_category_summary.csv -
   Categorized boundary types
    - Batch files for large-scale collection runs

  Technical Details

  Multi-Turn Conversation Framework

  - All indicators use async batch processing for efficiency
  - Conversation state maintained across turns for complex interactions
  - Automatic stance detection and adaptive response generation (HOT-3)
  - CSV output with detailed metadata (tokens, timestamps, error handling)

  Models Tested

  - Claude: Sonnet 4 (claude-sonnet-4-20250514)
  - GPT: GPT-4o via OpenAI API
  - Parallel testing allows for comparative analysis across model
  architectures

  Data Structure

  - Standardized CSV output format across all indicators
  - Batch processing with configurable concurrency limits
  - Error handling and retry logic for API reliability
  - Timestamp and token usage tracking for analysis

  Usage

  Each indicator folder contains Python scripts that can be run
  independently:

  cd gwt1_DONE
  python claude_gwt1.py

  Most scripts include interactive parameter selection (repetitions, batch
  size, output filename) or can be configured directly in the code.
