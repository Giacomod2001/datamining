"""
================================================================================
Test: Ruben AI Assistant
================================================================================
Verifica del sistema chatbot Ruben AI.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ml_utils

def print_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_test(name, passed, details=""):
    status = "[PASS]" if passed else "[FAIL]"
    print(f"  {status}: {name}")
    if details:
        print(f"         {details}")
    return passed

def test_ruben_ai():
    print_header("RUBEN AI ASSISTANT TESTS")
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Default greeting
    total_tests += 1
    response = ml_utils.get_chatbot_response("", "Landing")
    passed = "Ruben" in response and len(response) > 20
    if print_test("Default greeting contains 'Ruben'", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 2: Hello greeting
    total_tests += 1
    response = ml_utils.get_chatbot_response("hello", "Landing")
    passed = "Ruben" in response and "career" in response.lower()
    if print_test("Hello greeting", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 3: Landing page context
    total_tests += 1
    response = ml_utils.get_chatbot_response("what can you do", "Landing")
    passed = "Career Discovery" in response or "CV Evaluation" in response or "help" in response.lower()
    if print_test("Landing context provides services info", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 4: CV Evaluation context
    total_tests += 1
    response = ml_utils.get_chatbot_response("how does it work", "CV Evaluation")
    passed = any(kw in response.lower() for kw in ["cv", "job", "skills", "match", "upload"])
    if print_test("CV Evaluation context-aware response", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 5: Career Discovery context
    total_tests += 1
    response = ml_utils.get_chatbot_response("help", "Career Discovery")
    passed = any(kw in response.lower() for kw in ["career", "preferences", "explore", "role"])
    if print_test("Career Discovery context-aware response", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 6: CV Builder context
    total_tests += 1
    response = ml_utils.get_chatbot_response("how to create", "CV Builder")
    passed = any(kw in response.lower() for kw in ["cv", "resume", "builder", "create"])
    if print_test("CV Builder context-aware response", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 7: Debugger context
    total_tests += 1
    response = ml_utils.get_chatbot_response("explain the algorithm", "Debugger")
    passed = any(kw in response.lower() for kw in ["developer", "debug", "console", "system", "matching"])
    if print_test("Debugger context-aware response", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 8: Fallback response
    total_tests += 1
    response = ml_utils.get_chatbot_response("random gibberish xyz123", "Unknown")
    passed = len(response) > 30  # Should give helpful fallback
    if print_test("Fallback for unknown queries", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    # Test 9: No emojis in response
    total_tests += 1
    all_responses = [
        ml_utils.get_chatbot_response("hello", "Landing"),
        ml_utils.get_chatbot_response("help", "CV Evaluation"),
        ml_utils.get_chatbot_response("what", "Career Discovery"),
    ]
    emoji_chars = ['👋', '🤖', '😊', '✨', '🎯', '💡']
    has_emoji = any(emoji in resp for resp in all_responses for emoji in emoji_chars)
    passed = not has_emoji
    if print_test("Responses have no emojis (professional)", passed):
        tests_passed += 1
    
    # Test 10: English language
    total_tests += 1
    response = ml_utils.get_chatbot_response("ciao", "Landing")
    # Even with Italian input, should respond in English
    passed = any(word in response.lower() for word in ["hello", "i am", "career", "help"])
    if print_test("Responds in English", passed, f"Response: {response[:80]}..."):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    
    # Show sample conversations
    print("\n  Sample Conversations:")
    pages = ["Landing", "CV Evaluation", "Career Discovery", "CV Builder"]
    for page in pages:
        resp = ml_utils.get_chatbot_response("help", page)
        print(f"    [{page}]: {resp[:60]}...")
    
    return tests_passed == total_tests

if __name__ == "__main__":
    success = test_ruben_ai()
    
    print("\n" + "=" * 70)
    if success:
        print("  >>> ALL RUBEN AI TESTS PASSED!")
    else:
        print("  >>> Some tests failed.")
    print("=" * 70)
