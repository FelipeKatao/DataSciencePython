import Oct8 from "./Oct8/Oct8.js"
import ReadData from "./service/ReadDataFIle.js"

let oct8 = new Oct8()
let rd = new ReadData("main")

oct8.CreateObjectFactory(()=>{ 
let Object = oct8.CreateContainerElement("Main_page","pagina",'ArticleData','div')
oct8.ModifyPropsDefault(Object,null,null,null,null)
oct8.ModifyContentContainer(Object,""+
"<div><img id='Example'></div>"+
"<article class='articleColGraph'>"+
"</article>")
let ArticleGet = document.getElementsByClassName("articleColGraph")[0]
rd.CallData("main",ArticleGet,ArticleGet,document.getElementById("Example"))
}
,"MainPage")

oct8.AppendObjectFacyotyTo("MainPage",null)

