import os
from flask import Flask, request, jsonify
from backend.generate_blog import generate_blog

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_blog_endpoint():
    """Handles blog generation requests."""
    data = request.json
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    blog = generate_blog(topic)

    # Save to file
    blog_filename = f"blogs/{topic.replace(' ', '_').lower()}.md"
    with open(blog_filename, "w", encoding="utf-8") as f:
        f.write(blog)

    return jsonify({"message": "Blog generated successfully!", "blog": blog})

if __name__ == "__main__":
    os.makedirs("blogs", exist_ok=True)
    app.run(debug=True)


