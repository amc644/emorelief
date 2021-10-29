/* FUNCTION TO CHANGE THE OPTIONS IN THE DASHBOARDS */
function changeOption(sideBarOption,sideBarSelectedOption,content,selectedOption)
{
    /* CHANGE COLOR IN DE SIDE BAR WHEN SELECTED */
    var sideBarList=document.getElementsByClassName(sideBarOption);
    for(var a=0;a<sideBarList.length;a++)
    {
        sideBarList[a].setAttribute("style",".sideBar a:hover{background-color: rgb(104,104,104);color:rgb(53,53,53);}'");
    }
    document.getElementById(sideBarSelectedOption).style.backgroundColor='rgb(112, 11, 151)';

    /* CHANGE MAIN CONTENT */
    var contents=document.getElementsByClassName(content)
    for(var a=0;a<contents.length;a++)
    {
        contents[a].style.display='none';
    }
    document.getElementById(selectedOption).style.display='block';
}

function logOut() {
    if(confirm('Are you sure you want to log out?')) {
        window.location.href = 'home.html';
    }
}