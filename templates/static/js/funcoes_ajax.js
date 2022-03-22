function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type:'POST',
        url:'/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text(result.mensagem);
            $("#horas_utilizadas").text(result.horas);
        }

    });
    
}

function desmarcarHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type:'POST',
        url:'/horas-extras/desmarcou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text(result.mensagem);
            $("#horas_utilizadas").text(result.horas);
        }

    });
    
}

function testejs(){
    alert('teste.logs');
}