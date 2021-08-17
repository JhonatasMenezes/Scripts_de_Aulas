// Medidor de Velocidade
radarVelocidade(135);

function radarVelocidade(vel){
    let velMax = 70;
    let kmPorPonto = 5;
    let limitePontos = 12;
    let aMais = Math.floor((vel - velMax) / kmPorPonto);
    if(vel <= velMax)
        return console.log('Está dentro do limite de velocidade!');
    else if (vel > velMax){
            if(aMais > limitePontos){
            console.log('Velocidade excedida. Pontos: ', aMais);
            return console.log('Carteira Suspensa!');
        }
        return console.log('Velocidade excedida. Pontos: ', aMais);
    }
}
