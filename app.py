from flask import Flask, render_template, request

app = Flask(__name__)

medias_referencia = {
    2: 8.82,
    3: 13.23,
    4: 17.64,
    5: 22.06
}

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None

    if request.method == "POST":
        try:
            gasto_mensal = float(request.form.get("gasto_mensal"))
            tamanho_familia = int(request.form.get("tamanho_familia"))
            mes1 = float(request.form.get("mes1"))
            mes2 = float(request.form.get("mes2"))
            mes3 = float(request.form.get("mes3"))

            media_consumo = (mes1 + mes2 + mes3) / 3
            media_ref = medias_referencia.get(tamanho_familia, 0)

            if media_consumo > media_ref:
                status = "⚠️ Acima da média"
            elif media_consumo < media_ref:
                status = "✅ Abaixo da média - continue assim!"
            else:
                status = "ℹ️ Na média"

            custo_por_m3 = gasto_mensal / media_consumo

            resultado = {
                "media_consumo": f"{media_consumo:.2f}",
                "media_ref": f"{media_ref:.2f}",
                "status": status,
                "custo_por_m3": f"{custo_por_m3:.2f}"
            }

        except Exception as e:
            resultado = {"erro": f"Erro no processamento: {e}"}

    return render_template("calculadora.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)