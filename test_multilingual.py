"""
================================================================================
Test: Ruben AI Multilingual Support
================================================================================
Verifica del supporto multilingue per Ruben AI.
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

def test_language_detection():
    print_header("LANGUAGE DETECTION TESTS")
    
    tests_passed = 0
    total_tests = 0
    
    # Test Italian detection
    total_tests += 1
    lang = ml_utils._detect_chat_language("Ciao, come posso usare questo strumento?")
    passed = lang == 'it'
    if print_test(f"Italian detected: {lang}", passed):
        tests_passed += 1
    
    # Test Spanish detection
    total_tests += 1
    lang = ml_utils._detect_chat_language("Hola, necesito ayuda con mi curriculum")
    passed = lang == 'es'
    if print_test(f"Spanish detected: {lang}", passed):
        tests_passed += 1
    
    # Test French detection
    total_tests += 1
    lang = ml_utils._detect_chat_language("Bonjour, comment puis-je analyser mon CV?")
    passed = lang == 'fr'
    if print_test(f"French detected: {lang}", passed):
        tests_passed += 1
    
    # Test German detection
    total_tests += 1
    lang = ml_utils._detect_chat_language("Hallo, wie kann ich meinen Lebenslauf verbessern?")
    passed = lang == 'de'
    if print_test(f"German detected: {lang}", passed):
        tests_passed += 1
    
    # Test Portuguese detection
    total_tests += 1
    lang = ml_utils._detect_chat_language("Olá, preciso de ajuda com meu curriculo")
    passed = lang == 'pt'
    if print_test(f"Portuguese detected: {lang}", passed):
        tests_passed += 1
    
    # Test English default
    total_tests += 1
    lang = ml_utils._detect_chat_language("Hello, how does this work?")
    passed = lang == 'en'
    if print_test(f"English detected: {lang}", passed):
        tests_passed += 1
    
    # Test ambiguous falls to English
    total_tests += 1
    lang = ml_utils._detect_chat_language("xyz123")
    passed = lang == 'en'
    if print_test(f"Ambiguous defaults to English: {lang}", passed):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"


def test_multilingual_responses():
    print_header("MULTILINGUAL RESPONSE TESTS")
    
    tests_passed = 0
    total_tests = 0
    
    # Test Italian response
    total_tests += 1
    response = ml_utils.get_chatbot_response("Ciao, aiutami", "Landing")
    passed = any(w in response.lower() for w in ["sono", "ruben", "aiutarti", "ciao"])
    if print_test("Italian greeting response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test Spanish response
    total_tests += 1
    response = ml_utils.get_chatbot_response("Hola, necesito ayuda", "Landing")
    passed = any(w in response.lower() for w in ["soy", "ruben", "ayudar", "hola"])
    if print_test("Spanish greeting response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test French response
    total_tests += 1
    response = ml_utils.get_chatbot_response("Bonjour, aidez-moi", "Landing")
    passed = any(w in response.lower() for w in ["suis", "ruben", "aider", "bonjour"])
    if print_test("French greeting response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test German response
    total_tests += 1
    response = ml_utils.get_chatbot_response("Hallo, hilf mir bitte", "Landing")
    passed = any(w in response.lower() for w in ["bin", "ruben", "helfen", "hallo"])
    if print_test("German greeting response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test Portuguese response
    total_tests += 1
    response = ml_utils.get_chatbot_response("Olá, preciso de ajuda", "Landing")
    passed = any(w in response.lower() for w in ["sou", "ruben", "ajudar", "olá"])
    if print_test("Portuguese greeting response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test English default
    total_tests += 1
    response = ml_utils.get_chatbot_response("Hello there", "Landing")
    passed = "I am Ruben" in response or "Hello" in response
    if print_test("English default response", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test context-aware Italian
    total_tests += 1
    response = ml_utils.get_chatbot_response("Come funziona la valutazione?", "CV Evaluation")
    passed = any(w in response.lower() for w in ["cv", "carica", "competenze", "profilo"])
    if print_test("Italian CV Evaluation context", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    # Test context-aware Italian for Discovery
    total_tests += 1
    response = ml_utils.get_chatbot_response("Vorrei esplorare le carriere", "Career Discovery")
    passed = any(w in response.lower() for w in ["carriera", "percorsi", "preferenze", "ruoli"])
    if print_test("Italian Career Discovery context", passed, f"Response: {response[:60]}..."):
        tests_passed += 1
    
    print(f"\n  Summary: {tests_passed}/{total_tests} tests passed")
    assert tests_passed == total_tests, f"Failed {total_tests - tests_passed} tests"


def show_demo_conversations():
    print_header("DEMO: MULTILINGUAL CONVERSATIONS")
    
    test_messages = [
        ("Hello, how can I use this?", "English"),
        ("Ciao, come posso usare questo?", "Italian"),
        ("Hola, como puedo usar esto?", "Spanish"),
        ("Bonjour, comment utiliser ceci?", "French"),
        ("Hallo, wie kann ich das benutzen?", "German"),
        ("Ola, como posso usar isso?", "Portuguese"),
    ]
    
    for msg, lang in test_messages:
        response = ml_utils.get_chatbot_response(msg, "Landing")
        print(f"\n  [{lang}]")
        print(f"    User: {msg}")
        print(f"    Ruben: {response[:80]}...")


if __name__ == "__main__":
    success1 = test_language_detection()
    success2 = test_multilingual_responses()
    
    show_demo_conversations()
    
    print("\n" + "=" * 70)
    if success1 and success2:
        print("  >>> ALL MULTILINGUAL TESTS PASSED!")
    else:
        print("  >>> Some tests failed.")
    print("=" * 70)
