from deepl import DeepL
import asyncio

async def main():
    t = DeepL("ru", "en")
    translate_text = await t.translate("Здравствуйте")
    print(translate_text)

if __name__ == "__main__":
    asyncio.run(main())
