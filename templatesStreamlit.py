css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}


.main {
    padding: 2rem;
}

.skill {
    background-color: rgb(59, 59, 59);
    padding: 1rem 2rem;
    border-radius: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2rem;
    box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.3);
    transition: .3s;
}

.skill:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.skill-content {
    display: flex;
    align-items: center;
    width: 80%;
}

.skill-img-box {
  position: relative;
  min-width: 140px;
  height: 140px;
  margin-right: 2rem;
  border-radius: 1rem;
  background-size: cover; /* Ajusta el tamaño de la imagen para cubrir completamente el contenedor */
  background-position: center; /* Centra la imagen en el contenedor */
}

.skill-img-box img {
  width: 100%; /* Asegura que la imagen ocupe todo el espacio disponible en el contenedor */
  height: 100%;
  border-radius: 1rem;
  object-fit: cover; /* Ajusta el tamaño de la imagen manteniendo la proporción */
}

.skill-detail {
    width: 100%;
}

.skill-progress {
    position: relative;
    height: 1rem;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 1rem;
    overflow: hidden;
}

.progress {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background-color: #ffffff;
}


.chat-row {
    display: flex;
    margin: 5px;
    width: 100%;
}

.row-reverse {
    flex-direction: row-reverse;
}

.chat-box {
  max-width: 400px;
  margin: 20px auto;
  background-color: #8a8787;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}


.chat-bubble {
    font-family: "Source Sans Pro", sans-serif, "Segoe UI", "Roboto", sans-serif;
    border: 1px solid transparent;
    padding: 5px 10px;
    margin: 0px 7px;
    max-width: 70%;
}

.ai-bubble {
    background: rgb(153, 153, 153);
    border-radius: 10px;
}

.human-bubble {
    background: linear-gradient(135deg, rgb(0, 178, 255) 0%, rgb(0, 106, 255) 100%); 
    color: white;
    border-radius: 20px;
}

.chat-icon {
    border-radius: 5px;
}

.container-neon {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh; /* Ajusta la altura según tus necesidades o utiliza otro método para centrar verticalmente */
}

.btn-neon {
    position: relative;
    display: inline-block;
    padding: 15px 30px;
    color: #fff;
    letter-spacing: 4px;
    text-decoration: none;
    font-size: 44px;
    overflow: hidden;
    border-radius: 15px;
    # background: #a945c7;
    # box-shadow: 0 0 10px #a945c7, 0 0 40px #a945c7, 0 0 80px #a945c7;
    transition: 0.2s;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px rgba(255, 255, 255, 0.8), 0 0 30px rgba(255, 255, 255, 0.8);
}

.icon img {
    margin-right: 1px; /* Ajusta el espacio entre la imagen y el texto según tus necesidades */
    width: 30px; /* Ajusta el ancho de la imagen según tus necesidades */
    height: 30px; /* Ajusta la altura de la imagen según tus necesidades */
}


'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
bot_template2 = '''

<div class="chat-row">
    <img class="chat-icon" src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" width=45 height=45>
    <div class="chat-bubble ai-bubble">
        &#8203;{{MSG}}
    </div>
</div>

'''
user_template2 = '''

<div class="chat-row row-reverse">
    <img class="chat-icon" src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" width=45 height=45>
    <div class="chat-bubble human-bubble">
        &#8203;{{MSG}}
    </div>
</div>

'''



user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''