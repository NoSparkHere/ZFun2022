from flask import Flask, render_template, request

app = Flask(__name__)

correct_answers = [
    "明日方舟",
    "福建省福州市连江县凤城镇八一六东路223号",
    "XDSEC",
    "Gibson Les Paul Custom",
    "418",
    "1145141919810",
]

correct_flags = [
    "ZFun{WoW_3_Pro6lEms_5olveD!}",
    "ZFun{Meow_Ca7S_ArE_CUT3!!!}",
    "ZFun{Nya_N0t_7hAt_Ha2D!!!}",
]


@app.route("/", methods=["GET", "POST"])
def index():
    ctx = {"answered": False, "correct": 0, "extra": False, "flags": []}
    if request.method == "POST":
        answers = request.form
        flags = []
        correct = [False] * 6

        for i in range(len(correct_answers)):
            id = "question" + str(i + 1)
            if answers[id] == correct_answers[i]:
                correct[i] = True

        if correct[:5].count(True) >= 3:
            flags.append(correct_flags[0])
        if correct[:5].count(True) == 5:
            flags.append(correct_flags[1])
        if correct[5]:
            flags.append(correct_flags[2])

        ctx["answered"] = True
        ctx["correct"] = correct.count(True)
        ctx["extra"] = correct[5]
        ctx["flags"] = flags

    return render_template("index.html", ctx=ctx)
