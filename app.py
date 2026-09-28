from flask import Flask, render_template_string

app = Flask(__name__)

# بنك الأسئلة الشامل (يشمل اختيار من متعدد + صح وخطأ) لمنصة سر التفوق
questions = [
    # أسئلة اختيار من متعدد
    { "id": 1, "type": "mcq", "level": "مبتدئ", "question": "ما هي عاصمة مملكة معين في شبه الجزيرة العربية؟", "options": ["مأرب", "قرناو", "ريدان ظفار", "الجابية"], "answer": 1, "explanation": "عاصمة مملكة معين هي مدينة قرناو في منطقة الجوف باليمن." },
    { "id": 2, "type": "mcq", "level": "مبتدئ", "question": "من هي الملكة التي ورد ذكرها في القرآن الكريم في سورة النمل واشتهرت بحكمها لمملكة سبأ؟", "options": ["زنوبيا", "بلقيس", "السيدة خديجة", "جبلة"], "answer": 1, "explanation": "الملكة بلقيس هي ملكة سبأ الوارد ذكرها في القرآن الكريم." },
    { "id": 3, "type": "mcq", "level": "مبتدئ", "question": "أين تقع عاصمة مملكة حمير (ريدان ظفار)؟", "options": ["بين مملكة سبأ وبحر القلزم", "في بادية الشام بالجولان", "جنوب الكوفة غرب الفرات", "في منطقة الجوف باليمن"], "answer": 0, "explanation": "تقع عاصمة مملكة حمير بين مملكة سبأ وبحر القلزم (البحر الأحمر)." },
    { "id": 4, "type": "mcq", "level": "مبتدئ", "question": "ما أشهر قبائل مكة المكرمة قبل الإسلام؟", "options": ["الأوس", "الخزرج", "قريش", "ثقيف"], "answer": 2, "explanation": "تعد قبيلة قريش أشهر قبائل مكة المكرمة." },
    { "id": 5, "type": "mcq", "level": "مبتدئ", "question": "أي القبائل الآتية سكنت يثرب بعد انهيار سد مأرب؟", "options": ["قريش وثقيف", "الأوس والخزرج", "الغساسنة والحيرة", "معين وحمير"], "answer": 1, "explanation": "سكنت قبيلتا الأوس والخزرج يثرب بعد هجرتهما إثر انهيار سد مأرب." },

    # أسئلة صح وخطأ
    { "id": 6, "type": "tf", "level": "مبتدئ", "question": "تعددت عواصم الغساسنة وكان آخرها مدينة الجابية في الجولان.", "options": ["صح", "خطأ"], "answer": 0, "explanation": "عبارة صحيحة، كانت الجابية آخر عواصم الغساسنة في بادية الشام." },
    { "id": 7, "type": "tf", "level": "مبتدئ", "question": "كانت مملكة الحيرة تابعة للدولة البيزنطية (الروم) وتدين بالولاء لها.", "options": ["صح", "خطأ"], "answer": 1, "explanation": "عبارة خاطئة، مملكة الحيرة كانت تابعة للدولة الساسانية (الفارسية) وليس البيزنطية." },
    { "id": 8, "type": "tf", "level": "مبتدئ", "question": "العرب العدنانيون ينحدرون من نسل النبي إسماعيل بن إبراهيم عليهما السلام.", "options": ["صح", "خطأ"], "answer": 0, "explanation": "عبارة صحيحة، ترتفع نسب قبائل العرب العدنانية إلى النبي إسماعيل عليه السلام." },
    { "id": 9, "type": "tf", "level": "متوسط", "question": "تميزت مدينة الطائف قبل الإسلام بمناخها الحار جداً واتهارها بزراعة النخيل فقط.", "options": ["صح", "خطأ"], "answer": 1, "explanation": "عبارة خاطئة، الطائف تميزت بمناخ معتدل لارتفاع سطحها واشتهرت بزراعة العنب." },
    { "id": 10, "type": "tf", "level": "متوسط", "question": "ساد النظام القبلي القائم على العصبية والشيخ في مناطق البادية قبل الإسلام.", "options": ["صح", "خطأ"], "answer": 0, "explanation": "عبارة صحيحة، كان النظام القبلي هو السائد في مناطق البادية." }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة سر التفوق التعليمية</title>
    <style>
        body { font-family: 'Cairo', Tahoma, sans-serif; background-color: #f4f7f6; margin: 0; padding: 0; color: #333; }
        .container { max-width: 800px; margin: 50px auto; background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #1b4332; text-align: center; margin-bottom: 5px; }
        .subtitle { text-align: center; color: #6c757d; margin-bottom: 25px; font-size: 14px; }
        .rules-box { background: #e9f5ed; border-right: 5px solid #2d6a4f; padding: 15px 20px; margin-bottom: 25px; border-radius: 4px; }
        .rules-box h3 { margin-top: 0; color: #2d6a4f; }
        .rules-box ul { padding-right: 20px; margin-bottom: 0; }
        .btn { background-color: #2d6a4f; color: white; border: none; padding: 12px 25px; font-size: 16px; border-radius: 6px; cursor: pointer; display: block; width: 100%; text-align: center; font-weight: bold; transition: background 0.3s; }
        .btn:hover { background-color: #1b4332; }
        .question-card { display: none; }
        .question-card.active { display: block; }
        .question-title { font-size: 18px; font-weight: bold; margin-bottom: 20px; color: #1b4332; }
        .option-item { background: #f8f9fa; border: 2px solid #dee2e6; padding: 12px 15px; margin-bottom: 10px; border-radius: 6px; cursor: pointer; transition: all 0.2s; }
        .option-item:hover { background: #e2e8f0; border-color: #cbd5e1; }
        .option-item input { margin-left: 10px; }
        .result-box { display: none; }
        .result-item { background: #f8f9fa; padding: 15px; margin-bottom: 15px; border-radius: 6px; border-right: 4px solid #6c757d; }
        .result-item.correct { border-right-color: #2d6a4f; background: #f0fdf4; }
        .result-item.incorrect { border-right-color: #dc2626; background: #fef2f2; }
        .score-display { text-align: center; font-size: 24px; font-weight: bold; color: #2d6a4f; margin-bottom: 20px; }
        .badge { background: #e2e8f0; color: #1b4332; padding: 3px 8px; border-radius: 4px; font-size: 11px; margin-left: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>منصة سر التفوق التعليمية</h1>
        <div class="subtitle">بنك أسئلة تاريخ وتراث شبه الجزيرة العربية (اختيار من متعدد + صح وخطأ)</div>

        <!-- الصفحة الرئيسية وقواعد الاختبار -->
        <div id="home-screen">
            <div class="rules-box">
                <h3>تعليمات وقواعد الاختبار:</h3>
                <ul>
                    <li>يحتوي الاختبار على مزيج من أسئلة <strong>الاختيار من متعدد</strong> وأسئلة <strong>صح وخطأ</strong>.</li>
                    <li>أجب عن جميع الأسئلة بالانتقال بمرونة بينها عبر الأزرار المتاحة.</li>
                    <li><strong>لن يتم إظهار التصحيح الفوري أو النتائج أثناء حل الأسئلة</strong>.</li>
                    <li>سيتم مراجعة الدرجات، وتوضيح الإجابات الصحيحة والخاطئة **في نهاية الاختبار فقط** تماماً كما اتفقنا.</li>
                </ul>
            </div>
            <button class="btn" onclick="startQuiz()">ابدأ الاختبار الآن</button>
        </div>

        <!-- شاشة الأسئلة -->
        <div id="quiz-screen" style="display: none;">
            <div id="questions-container"></div>
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <button class="btn" id="prev-btn" onclick="prevQuestion()" style="width: 48%; background-color: #6c757d; display: none;">السابق</button>
                <button class="btn" id="next-btn" onclick="nextQuestion()" style="width: 100%;">السؤال التالي</button>
            </div>
        </div>

        <!-- شاشة النتيجة النهائية والتصحيح في الآخر -->
        <div id="result-screen" class="result-box">
            <div class="score-display" id="score-text"></div>
            <h3>مراجعة الإجابات والتصحيح الشامل:</h3>
            <div id="review-container"></div>
            <button class="btn" onclick="location.reload()" style="margin-top: 20px;">إعادة الاختبار</button>
        </div>
    </div>

    <script>
        const questions = {{ questions | tojson }};
        let currentIdx = 0;
        let userAnswers = {};

        function startQuiz() {
            document.getElementById('home-screen').style.display = 'none';
            document.getElementById('quiz-screen').style.display = 'block';
            renderQuestion();
        }

        function renderQuestion() {
            const container = document.getElementById('questions-container');
            const q = questions[currentIdx];
            
            let typeBadge = q.type === 'tf' ? 'صح وخطأ' : 'اختيار من متعدد';
            
            let html = `
                <div class="question-card active">
                    <div style="font-size: 12px; color: #2d6a4f; font-weight: bold; margin-bottom: 5px;">
                        السؤال ${currentIdx + 1} من ${questions.length} 
                        <span class="badge">${typeBadge}</span> 
                        <span class="badge">${q.level}</span>
                    </div>
                    <div class="question-title">${q.question}</div>
            `;
            
            q.options.forEach((opt, idx) => {
                let checked = userAnswers[currentIdx] === idx ? 'checked' : '';
                html += `
                    <label class="option-item" style="display: block;">
                        <input type="radio" name="q${currentIdx}" value="${idx}" ${checked} onclick="saveAnswer(${currentIdx}, ${idx})">
                        ${opt}
                    </label>
                `;
            });
            
            html += `</div>`;
            container.innerHTML = html;

            document.getElementById('prev-btn').style.display = currentIdx > 0 ? 'inline-block' : 'none';
            const nextBtn = document.getElementById('next-btn');
            if (currentIdx === questions.length - 1) {
                nextBtn.innerText = "إنهاء الاختبار وعرض النتيجة";
            } else {
                nextBtn.innerText = "السؤال التالي";
            }
        }

        function saveAnswer(qIdx, optIdx) {
            userAnswers[qIdx] = optIdx;
        }

        function nextQuestion() {
            if (userAnswers[currentIdx] === undefined) {
                alert('الرجاء اختيار إجابة قبل الانتقال للسؤال التالي.');
                return;
            }
            if (currentIdx < questions.length - 1) {
                currentIdx++;
                renderQuestion();
            } else {
                showResults();
            }
        }

        function prevQuestion() {
            if (currentIdx > 0) {
                currentIdx--;
                renderQuestion();
            }
        }

        function showResults() {
            document.getElementById('quiz-screen').style.display = 'none';
            document.getElementById('result-screen').style.display = 'block';

            let score = 0;
            let reviewHtml = '';

            questions.forEach((q, idx) => {
                const userAns = userAnswers[idx];
                const isCorrect = userAns === q.answer;
                if (isCorrect) score++;

                const userText = userAns !== undefined ? q.options[userAns] : 'لم تقم بالإجابة';
                const correctText = q.options[q.answer];

                reviewHtml += `
                    <div class="result-item ${isCorrect ? 'correct' : 'incorrect'}">
                        <strong>السؤال ${idx + 1}:</strong> ${q.question}<br>
                        <strong>إجابتك:</strong> ${userText} ${isCorrect ? '✅' : '❌'}<br>
                        ${!isCorrect ? `<strong>الإجابة الصحيحة:</strong> ${correctText}<br>` : ''}
                        <small style="color: #555; display: block; margin-top: 5px;"><strong>التوضيح:</strong> ${q.explanation}</small>
                    </div>
                `;
            });

            document.getElementById('score-text').innerText = `نتيجتك النهائية: ${score} من ${questions.length}`;
            document.getElementById('review-container').innerHTML = reviewHtml;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, questions=questions)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
