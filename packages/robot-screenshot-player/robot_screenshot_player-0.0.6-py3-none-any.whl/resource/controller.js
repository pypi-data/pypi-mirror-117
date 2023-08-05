var current_imageworkflow_path=''
var id_of_anchor_link=-1
var interval
var current_image_index=0
var period_for_image_update=1000
var  image_json_container=typeof image_json_container1 === 'undefined'?{}:image_json_container1


function displayNextImage() {
   if(image_json_container[id_of_anchor_link][1].length<=current_image_index) {
        current_image_index=0
        clearInterval(interval)
        interval=null
        console.log("end of the image")
        return
}
let image_src=`${current_imageworkflow_path}${image_json_container[id_of_anchor_link][1][current_image_index]}`
document.getElementById("img").src = image_src
document.getElementById("myBar").style.width=(current_image_index/image_json_container[id_of_anchor_link][1].length)*100+'%'
// console.log(image_src)
current_image_index++


}
function update_time(text){
document.getElementById("interval_in_ms").textContent=text+'ms'
}

function populate_sideBar_for_various_workflow(){
let sidebar=document.getElementById("sidebar")
for(let item in image_json_container){
    link=document.createElement("a")
    link.text = image_json_container[item][0].split("\\").reverse()[0]
    link.href='#'
    link.id=item
    link.onclick= function(event) {
        if(interval){
            clearInterval(interval)
            interval=null
        }
        current_image_index=0
        id_of_anchor_link=event.target.id
        current_imageworkflow_path=`${image_json_container[event.target.id][0]}/`
        interval=setInterval(displayNextImage, period_for_image_update);
        console.log(id_of_anchor_link)
    }
  
   
    sidebar.appendChild(link)
    
}
}
function startTimer() {

populate_sideBar_for_various_workflow()
update_time(period_for_image_update)


}

function pause(){
if(interval){
    clearInterval(interval);
    interval=null
}
}

function resume(){
console.log(!interval)
console.log(current_image_index+"----- in resume")
if (!interval)
{
    interval=setInterval(displayNextImage, period_for_image_update);
}
}
/**
* clearing setinterval  and setting  the frame to zero 
* */
function reset(){
if(interval!=null){
    clearInterval(interval);
    interval=null
    current_image_index=0
    document.getElementById("myBar").style.width=0
    document.getElementById("img").src = ''
    
}

}

function showNextFrame(){
  //only in pause state
  if(interval==null && id_of_anchor_link!=-1){
    displayNextImage()
  }
}

function showPrevFrame(){
  //only in pause state
  if(interval==null && id_of_anchor_link!=-1){
    current_image_index=current_image_index-2;
    displayNextImage()
  }
}

function speedConroller(speeding_factor){
period_for_image_update=period_for_image_update/speeding_factor
console.log(`Time lagging for two consecutive image is :`,period_for_image_update)
update_time(period_for_image_update)
if(interval!=null){
    clearInterval(interval)
    interval=setInterval(displayNextImage,period_for_image_update)
}
}





