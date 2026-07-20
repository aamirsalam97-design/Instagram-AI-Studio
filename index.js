import Groq from "groq-sdk";
import dotenv from "dotenv";

dotenv.config();

const groq = new Groq({
    apiKey: process.env.GROQ_API_KEY,
});

async function main() {
    const chatCompletion = await groq.chat.completions.create({
        model: "llama-3.3-70b-versatile",
        messages: [
            {
                role: "user",
                content: "Write an Instagram caption for a sunset photo with emojis and hashtags.",
            },
        ],
    });

    console.log(chatCompletion.choices[0].message.content);
}

main().catch(console.error);