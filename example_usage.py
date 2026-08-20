from client import MultiLanguageLivestreamHostTeleprompterScriptSynthesizerClient

def main():
    client = MultiLanguageLivestreamHostTeleprompterScriptSynthesizerClient()
    res = client.synthesize_teleprompter_cue("Does this work overseas with 220V power outlets?")
    print(f"Response Latency: {res['response_latency_ms']}ms")
    print(f"Teleprompter Cue: {res['instant_teleprompter_cue']}")
    print(f"Upsell Recommendation: {res['recommended_product_upsell']}")

if __name__ == "__main__":
    main()
