import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==================================================
# Caption Generator
# ==================================================

def generate_caption(image, style):

    prompt = f"""
You are an expert Instagram Content Creator.

Generate:

1. Five engaging Instagram captions
2. 30 trending hashtags
3. Image Category
4. Mood
5. Strong CTA

Caption Style:
{style}

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# Image Description
# ==================================================

def generate_image_description(objects):

    prompt = f"""
Detected Objects:

{objects}

Write:

1. Short Image Description

2. Instagram Caption

Return in markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# Engagement Predictor
# ==================================================

def predict_engagement(description):

    prompt = f"""
You are an Instagram Growth Expert.

Image Description:

{description}

Predict:

1. Expected Likes

2. Expected Comments

3. Engagement Rate

4. Viral Score (0-10)

5. Tips to improve engagement

Return in markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# Sentiment Analyzer
# ==================================================

def analyze_sentiment(comment):

    prompt = f"""
You are an AI Sentiment Analyzer.

Analyze this Instagram comment.

Comment:
{comment}

Return:

😊 Sentiment

📊 Confidence %

💡 Suggested Reply

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# Content Quality Analyzer
# ==================================================

def analyze_content_quality(caption):

    prompt = f"""
You are an Instagram Growth Expert.

Analyze this caption.

Caption:

{caption}

Return:

⭐ Content Score (0-100)

🔥 Viral Probability (%)

😊 Emotion

📈 Best Posting Time

💡 Five Suggestions to Improve

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# AI Reply Generator
# ==================================================

def generate_reply(comment):

    prompt = f"""
You are a professional Instagram creator.

Generate a friendly reply to this Instagram comment.

Comment:
{comment}

Requirements:
- Friendly
- Short
- Human-like
- Use emojis when appropriate

Return only the reply.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# AI Hashtag Generator
# ==================================================

def generate_hashtags(topic):

    prompt = f"""
Generate 30 trending Instagram hashtags.

Topic:
{topic}

Rules:
- Relevant hashtags only
- Mix of high, medium and low competition hashtags
- Return only hashtags in markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


# ==================================================
# AI Caption Improver
# ==================================================

def improve_caption(caption):

    prompt = f"""
You are an Instagram Growth Expert.

Improve the following Instagram caption.

Caption:
{caption}

Requirements:
- More engaging
- Better CTA
- Better readability
- Add suitable emojis
- Make it more likely to get engagement

Return only the improved caption in markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Caption Translator
# ==================================================

def translate_caption(caption, language):

    prompt = f"""
Translate the following Instagram caption into {language}.

Rules:
- Keep emojis.
- Keep formatting.
- Keep hashtags unchanged.
- Return only the translated caption.

Caption:

{caption}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Caption Improver
# ==================================================

def improve_caption(caption):

    prompt = f"""
You are an Instagram Growth Expert.

Improve the following Instagram caption.

Caption:
{caption}

Requirements:
- Make it more engaging
- Add suitable emojis
- Improve readability
- Add a strong Call-To-Action
- Keep it human-like

Return only the improved caption.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Reel Script Generator
# ==================================================

def generate_reel_script(topic, duration, tone):

    prompt = f"""
You are a professional Instagram Reel Creator.

Create a {duration}-second Instagram Reel.

Topic:
{topic}

Tone:
{tone}

Include:

1. Hook (First 3 seconds)
2. Full Reel Script
3. Voiceover Script
4. Camera Shot Suggestions
5. Call-To-Action
6. 15 Relevant Hashtags

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Competitor Analyzer
# ==================================================

def analyze_competitor(username):

    prompt = f"""
You are an Instagram Growth Consultant.

Analyze this Instagram account:

{username}

Provide:

1. Content Strategy
2. Posting Style
3. Target Audience
4. Hashtag Strategy
5. Strengths
6. Weaknesses
7. Growth Suggestions

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Instagram Profile Auditor
# ==================================================

def profile_audit(name, niche, bio):

    prompt = f"""
You are an Instagram Growth Consultant.

Audit the following Instagram profile.

Name:
{name}

Niche:
{niche}

Bio:
{bio}

Provide:

1. Overall Score (0-100)
2. Bio Review
3. Username Suggestions
4. Bio Improvement
5. Content Strategy
6. Posting Frequency
7. CTA Suggestions
8. Growth Tips

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Brand Collaboration Email Generator
# ==================================================

def generate_brand_email(creator, brand, niche, followers, tone):

    prompt = f"""
You are an expert Influencer Marketing Manager.

Generate a brand collaboration email.

Creator:
{creator}

Brand:
{brand}

Niche:
{niche}

Followers:
{followers}

Tone:
{tone}

Include:
1. Email Subject
2. Professional Email
3. Call to Action
4. Signature

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
# ==================================================
# AI Content Calendar
# ==================================================

def generate_content_calendar(topic):

    prompt = f"""
You are an Instagram Growth Expert.

Create a 7-day Instagram content calendar.

Topic:
{topic}

For each day include:

1. Post Idea
2. Caption Idea
3. Reel Idea
4. Story Idea
5. Best Posting Time

Return in beautiful markdown.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
