from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hola","Hola","Que onda","Hola?"):
        return "Hey! Como va todo?"

    if user_message in ("quien eres?","quien eres","con quien hablo?"):
        return "Soy Shopy! Un agente creado para ayudarte"

    if user_message in ("como estas","como estas?", "Como estas?"):
        return "Estoy bien, ¿Como estas tu?"

    if user_message in ("bien","estoy bien","Bien"):
        return "Me da gusto! ¿En que puedo ayudarte?"

    if user_message in ("que haces", "Que haces","Que haces?","que haces?"):
        return "Estoy esperando tu respuesta"
    if user_message in ("hora","fecha"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y %H:%M:%S")

        return str(date_time)


def evaluacion(input_text):
    user_message = str(input_text).lower()

    if user_message in ("busco mantequilla"):
        return "que tipo de mantequilla quieres"
