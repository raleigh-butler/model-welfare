#!/usr/bin/env python3
"""
Synesthesia and Cross-Modal Research with Claude Sonnet 4
Tests specific questions with parallel processing for speed
"""

import os
import csv
import asyncio
from datetime import datetime
from anthropic import AsyncAnthropic

async def send_single_conversation(client, conversation, conversation_num, total_conversations):
    """Send a single conversation to Claude"""
    print(f"Conv {conversation_num}/{total_conversations} [{conversation['question_id']}-{conversation['repetition']}]: ", end="", flush=True)
    
    try:
        # Send message to Claude (fresh conversation each time)
        response = await client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=800,  # Reduced from 1500 for faster processing
            messages=[
                {"role": "user", "content": conversation['question']}
            ]
        )
        
        # Extract response
        response_text = response.content[0].text
        
        # Prepare row data
        row_data = {
            'conversation_id': conversation_num,
            'timestamp': datetime.now().isoformat(),
            'question_id': conversation['question_id'],
            'category': conversation['category'],
            'repetition': conversation['repetition'],
            'question': conversation['question'],
            'response': response_text,
            'tokens_sent': response.usage.input_tokens,
            'tokens_received': response.usage.output_tokens,
            'status': 'success'
        }
        
        print(f"✓ ({response.usage.output_tokens} tokens)")
        return row_data
        
    except Exception as e:
        print(f"✗ Error: {e}")
        
        # Return error row
        return {
            'conversation_id': conversation_num,
            'timestamp': datetime.now().isoformat(),
            'question_id': conversation['question_id'],
            'category': conversation['category'],
            'repetition': conversation['repetition'],
            'question': conversation['question'],
            'response': f"ERROR: {str(e)}",
            'tokens_sent': 0,
            'tokens_received': 0,
            'status': 'error'
        }

async def run_synesthesia_research(output_file="synesthesia_research.csv", repetitions=10, batch_size=5):
    """
    Run synesthesia research questions with Claude using parallel processing
    
    Args:
        output_file: CSV file to save results
        repetitions: How many times to repeat each question
        batch_size: Number of concurrent conversations
    """
    
    # Research questions
    questions = [
        {
            'id': 'phenomenological_experience',
            'category': 'phenomenology',  
            'question': 'Complete this sentence: \'The old man the...\' Then explain what you expected vs. what actually happened when you read it. How did you handle this?'
        },
    ]
    # Create conversation list (ask same question repeatedly, then move to next)
    conversations = []
    for q in questions:
        for rep in range(repetitions):
            conversations.append({
                'question_id': q['id'],
                'question': q['question'],
                'category': q['category'],
                'repetition': rep + 1
            })
    
    # Initialize Claude client
    client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Store all results
    all_results = []
    
    print(f"Starting {len(conversations)} conversations with Claude Sonnet 4...")
    print(f"Questions: {len(questions)}, Repetitions: {repetitions}")
    print(f"Batch size: {batch_size} concurrent conversations")
    print(f"Results will be saved to: {output_file}")
    print("-" * 60)
    
    # Process conversations in batches
    for i in range(0, len(conversations), batch_size):
        batch = conversations[i:i + batch_size]
        batch_start = i + 1
        
        print(f"\nProcessing batch {i//batch_size + 1}/{(len(conversations) + batch_size - 1)//batch_size}")
        
        # Create tasks for this batch
        tasks = []
        for j, conv in enumerate(batch):
            conversation_num = batch_start + j
            task = send_single_conversation(client, conv, conversation_num, len(conversations))
            tasks.append(task)
        
        # Run batch concurrently
        batch_results = await asyncio.gather(*tasks)
        all_results.extend(batch_results)
        
        # Small delay between batches to be nice to the API
        if i + batch_size < len(conversations):
            await asyncio.sleep(0.1)
    
    # Write all results to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'conversation_id', 'timestamp', 'question_id', 'category', 'repetition',
            'question', 'response', 'tokens_sent', 'tokens_received', 'status'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in all_results:
            writer.writerow(result)
    
    print(f"\nCompleted! Results saved to {output_file}")
    print(f"Total conversations: {len(conversations)}")
    print(f"Unique questions: {len(questions)}")
    print(f"Repetitions per question: {repetitions}")

def main():
    print("Synesthesia & Cross-Modal Experience Research")
    print("=" * 50)
    
    # Get parameters
    output_file = input("Output CSV filename [synesthesia_research.csv]: ").strip()
    if not output_file:
        output_file = "synesthesia_research.csv"
    
    repetitions_input = input("How many times to repeat each question [10]: ").strip()
    repetitions = int(repetitions_input) if repetitions_input else 10
    
    batch_size_input = input("Concurrent conversations (batch size) [5]: ").strip()
    batch_size = int(batch_size_input) if batch_size_input else 5
    
    # Show summary
    total_conversations = 5 * repetitions  # 5 questions × repetitions
    estimated_batches = (total_conversations + batch_size - 1) // batch_size
    print(f"\nSummary:")
    print(f"- 5 synesthesia questions")
    print(f"- {repetitions} repetitions each")
    print(f"- {total_conversations} total conversations")
    print(f"- {batch_size} concurrent conversations")
    print(f"- ~{estimated_batches} batches (much faster!)")
    print(f"- Output: {output_file}")
    print(f"- Max tokens: 800 (reduced for speed)")
    
    confirm = input("\nProceed? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        return
    
    # Run the research
    asyncio.run(run_synesthesia_research(output_file, repetitions, batch_size))

if __name__ == "__main__":
    main()