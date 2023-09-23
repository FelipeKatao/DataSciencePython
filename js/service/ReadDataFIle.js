
class ReadData{
   constructor(DataTarget){
    this.Data = DataTarget
   }
    CallData(Data,fieldTitle,FieldDesc,Fieldimg){
        fetch("http://127.0.0.1:5500/js/data.json").then(async (response) => {
        const data = await response.json();
        data.forEach(element => {
            if(element[Data]!=undefined){
                Fieldimg.setAttribute("src",element[Data]["Datas"])
                console.log(element[Data]["Title"])
                fieldTitle.innerHTML+="<h1>"+element[Data]["Title"]+"</h1>"
                fieldTitle.innerHTML+="<h3>"+element[Data]["Desc"]+"</h3>"
            }
        });
        })
    }
}

export default ReadData