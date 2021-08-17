// Média escolar a partir de array

// 0 - 49: F
// 50 - 59: E
// 60 - 69: D
// 70 - 79: C
// 80 - 99: B
// 90 - 100: A

const array = [70, 70, 80];

console.log(mediaAluno(array));

function mediaAluno(notas){
    const notasLetra = ['A', 'B','C','D','E','F']
    const media = calculoMedia(notas);
    console.log(media);
    if(media < 59) return notasLetra[5];
    if(media < 59) return notasLetra[4];
    if(media < 69) return notasLetra[3];
    if(media < 79) return notasLetra[2];
    if(media < 89) return notasLetra[1];
    if(media < 100) return notasLetra[0];
}  


function calculoMedia(array){
    let media = 0;
    let qInd = 0;
    for(i in array){
        media += array[i];
        qInd += 1;
    }
    return media/qInd;
}