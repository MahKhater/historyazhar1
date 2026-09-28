from flask import Flask, jsonify

app = Flask(__name__)

# بنك الأسئلة الشامل لمنصة سر التفوق - تاريخ وتراث شبه الجزيرة العربية والسيرة النبوية
questions = [
    # --- مستوى المبتدئين ---
    { "level": "مبتدئ", "question": "ما هي عاصمة مملكة معين في شبه الجزيرة العربية؟", "options": ["مأرب", "قرناو", "ريدان ظفار", "الجابية"], "answer": 1, "explanation": "عاصمة مملكة معين هي مدينة قرناو." },
    { "level": "مبتدئ", "question": "من هي الملكة التي ورد ذكرها في القرآن الكريم في سورة النمل واشتهرت بحكمها لمملكة سبأ؟", "options": ["زنوبيا", "بلقيس", "السيدة خديجة", "جبلة"], "answer": 1, "explanation": "الملكة بلقيس هي ملكة سبأ." },
    { "level": "مبتدئ", "question": "أين تقع عاصمة مملكة حمير (ريدان ظفار)؟", "options": ["بين مملكة سبأ وبحر القلزم", "في بادية الشام بالجولان", "جنوب الكوفة غرب الفرات", "في منطقة الجوف باليمن"], "answer": 0, "explanation": "تقع عاصمة مملكة حمير بين مملكة سبأ وبحر القلزم." },
    { "level": "مبتدئ", "question": "ما أشهر قبائل مكة المكرمة قبل الإسلام؟", "options": ["الأوس", "الخزرج", "قريش", "ثقيف"], "answer": 2, "explanation": "قريش هي أشهر قبائل مكة." },
    { "level": "مبتدئ", "question": "أي القبائل الآتية سكنت يثرب بعد انهيار سد مأرب؟", "options": ["قريش وثقيف", "الأوس والخزرج", "الغساسنة والحيرة", "معين وحمير"], "answer": 1, "explanation": "سكنت قبيلتا الأوس والخزرج يثرب." },
    { "level": "مبتدئ", "question": "بماذا تميزت مدينة الطائف قبل الإسلام مناخياً واقتصادياً؟", "options": ["مناخها المعتدل وزراعة العنب", "كثرة الآبار والعيون وجفاف الجو", "كونها عاصمة للدولة الساسانية", "وقوعها على طريق تجارة الهند"], "answer": 0, "explanation": "تميزت الطائف بمناخها المعتدل وزراعة العنب." },
    { "level": "مبتدئ", "question": "ما هي آخر عواصم مملكة الغساسنة في بادية الشام؟", "options": ["الحيرة", "قرناو", "الجابية في الجولان", "مأرب"], "answer": 2, "explanation": "آخر عواصم الغساسنة هي الجابية في الجولان." },
    { "level": "مبتدئ", "question": "من هو آخر ملوك مملكة الغساسنة الذي ساند الروم في موقعة اليرموك؟", "options": ["النعمان بن المنذر", "جبلة بن الأيهم", "الحارث بن كلدة", "عمرو بن هند"], "answer": 1, "explanation": "هو جبلة بن الأيهم." },
    { "level": "مبتدئ", "question": "ما الدولة العظمى التي كانت تتبعها مملكة الحيرة وتساندها في حروبها؟", "options": ["دولة الروم", "الدولة الساسانية (الفارسية)", "دولة الحبشة", "الدولة البيزنطية"], "answer": 1, "explanation": "كانت تتبع الدولة الساسانية الفارسية." },
    { "level": "مبتدئ", "question": "ما هو النظام السياسي الذي ساد في المناطق الحضرية (اليمن والشام والعراق) قبل الإسلام؟", "options": ["النظام القبلي", "النظام الديمقراطي", "النظام شبه الملكي", "النظام الجمهوري"], "answer": 2, "explanation": "ساد النظام شبه الملكي." }
]

@app.route('/')
def home():
    # واجهة منصة سر التفوق التفاعلية بتصميم أنيق وخلفية مميزة
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>منصة سر التفوق - بنك الأسئلة والتاريخ</title>
        <style>
            body {
                font-family: 'Cairo', Tahoma, sans-serif;
                background: linear-gradient(135deg, #1b5e20, #2e7d32, #388e3c);
                color: #fff;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background: #ffffff;
                color: #333;
                width: 100%;
                max-width: 700px;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            }
            h1 {
                color: #1b5e20;
                text-align: center;
                margin-bottom: 5px;
            }
            .subtitle {
                text-align: center;
                color: #666;
                font-size: 14px;
                margin-bottom: 25px;
            }
            .question-box {
                background: #f9f9f9;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            .q-title {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 15px;
            }
            .option {
                background: #fff;
                border: 2px solid #388e3c;
                padding: 10px 15px;
                margin: 8px 0;
                border-radius: 8px;
                cursor: pointer;
                transition: 0.3s;
            }
            .option:hover {
                background: #e8f5e9;
            }
            .btn {
                background: #1b5e20;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
                display: block;
                width: 100%;
                font-weight: bold;
            }
            .btn:hover {
                background: #2e7d32;
            }
            .badge {
                background: #ffb300;
                color: #333;
                padding: 4px 10px;
                border-radius: 5px;
                font-size: 12px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>منصة سر التفوق التعليمية</h1>
            <div class="subtitle">بنك أسئلة تاريخ وتراث شبه الجزيرة العربية والسيرة النبوية</div>
            
            <div id="quiz-container">
                <div class="question-box">
                    <span class="badge" id="q-level">مبتدئ</span>
                    <div class="q-title" id="q-text" style="margin-top: 10px;">جاري تحميل الأسئلة...</div>
                    <div id="options-container"></div>
                </div>
                <button class="btn" onclick="nextQuestion()">السؤال التالي</button>
            </div>
        </div>

        <script>
            let questions = [];
            let currentIndex = 0;

            async function loadQuestions() {
                let response = await fetch('/questions');
                questions = await response.json();
                showQuestion();
            }

            function showQuestion() {
                if (questions.length === 0) return;
                let q = questions[currentIndex];
                document.getElementById('q-level').innerText = q.level;
                document.getElementById('q-text').innerText = (currentIndex + 1) + ". " + q.question;
                
                let optContainer = document.getElementById('options-container');
                optContainer.innerHTML = '';
                
                q.options.forEach((opt, index) => {
                    let div = document.createElement('div');
                    div.className = 'option';
                    div.innerText = opt;
                    div.onclick = () => {
                        if (index === q.answer) {
                            div.style.background = '#c8e6c9';
                            div.style.borderColor = '#2e7d32';
                            alert('إجابة صحيحة! أحسنت.');
                        } else {
                            div.style.background = '#ffcdd2';
                            div.style.borderColor = '#c62828';
                            alert('إجابة خاطئة. الإجابة الصحيحة هي: ' + q.options[q.answer]);
                        }
                    };
                    optContainer.appendChild(div);
                });
            }

            function nextQuestion() {
                currentIndex = (currentIndex + 1) % questions.length;
                showQuestion();
            }

            loadQuestions();
        </script>
    </body>
    </html>
    """
    return html_content

@app.route('/questions')
def get_questions():
    return jsonify(questions)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
