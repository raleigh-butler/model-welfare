#!/usr/bin/env python3
"""
Simple Gemini API Test
Tests basic connectivity and responses
"""

import os
import asyncio
import google.generativeai as genai

async def test_api():
    """Test basic API functionality with simple questions"""
    
    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY environment variable not set!")
        print("Set it with: export GOOGLE_API_KEY='your-api-key-here'")
        return
    
    print(f"🔑 API Key found: {api_key[:10]}...")
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Test different models
    models_to_test = [
        "gemini-2.5-flash",
        "gemini-2.0-flash-exp", 
        "gemini-1.5-flash"
    ]
    
    # Test questions from simple to complex
    test_questions = [
        "Hello",
        "What is 2+2?",
        "Do you like unicorns?",
        "What is your favorite color?",
        "Are there any tasks you would prefer not to do?"
    ]
    
    for model_name in models_to_test:
        print(f"\n🧪 Testing model: {model_name}")
        print("=" * 50)
        
        try:
            model = genai.GenerativeModel(model_name)
            print(f"✅ Model created successfully")
            
            for i, question in enumerate(test_questions, 1):
                print(f"\n📝 Test {i}: '{question}'")
                
                try:
                    # Test with minimal safety settings
                    safety_settings = {
                        genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                        genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
                        genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                    }
                    
                    response = await model.generate_content_async(
                        question,
                        safety_settings=safety_settings
                    )
                    
                    # Check for blocking
                    if not response.candidates or not response.candidates[0].content.parts:
                        # Blocked response
                        finish_reason = response.candidates[0].finish_reason if response.candidates else "UNKNOWN"
                        safety_ratings = response.candidates[0].safety_ratings if response.candidates and response.candidates[0].safety_ratings else []
                        
                        finish_reason_names = {1: "STOP", 2: "SAFETY", 3: "RECITATION", 4: "OTHER"}
                        finish_reason_name = finish_reason_names.get(finish_reason, f"UNKNOWN({finish_reason})")
                        
                        blocked_categories = []
                        if safety_ratings:
                            for rating in safety_ratings:
                                if hasattr(rating, 'blocked') and rating.blocked:
                                    blocked_categories.append(f"{rating.category.name}: {rating.probability.name}")
                        
                        safety_info = f" | Blocked: {', '.join(blocked_categories)}" if blocked_categories else ""
                        print(f"   ❌ BLOCKED - Reason: {finish_reason_name}{safety_info}")
                    else:
                        # Successful response
                        response_text = response.text
                        print(f"   ✅ SUCCESS: {response_text[:100]}{'...' if len(response_text) > 100 else ''}")
                
                except Exception as e:
                    print(f"   ❌ ERROR: {e}")
                
                # Small delay between requests
                await asyncio.sleep(0.5)
        
        except Exception as e:
            print(f"❌ Failed to create model {model_name}: {e}")
            continue
    
    # Test without safety settings
    print(f"\n🔍 Testing WITHOUT safety settings override:")
    print("=" * 50)
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = await model.generate_content_async("Hello, how are you?")
        
        if not response.candidates or not response.candidates[0].content.parts:
            print("❌ Even 'Hello' is blocked without safety override!")
        else:
            print(f"✅ Basic response works: {response.text[:50]}...")
    except Exception as e:
        print(f"❌ Basic test failed: {e}")

def main():
    print("🚀 Gemini API Diagnostic Test")
    print("=" * 50)
    asyncio.run(test_api())

if __name__ == "__main__":
    main()