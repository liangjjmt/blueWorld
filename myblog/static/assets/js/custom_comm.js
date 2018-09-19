function changeSideBarColor(item){
    var mainMenuList = $("#main-menu li a");
        var i = mainMenuList.length;
        while (i--) {
            if (i == item) {
                mainMenuList.eq(i).addClass("active-menu");
            } else {
                if(mainMenuList.eq(i).hasClass("active-menu")){
                    mainMenuList.eq(i).removeClass("active-menu");
                }                
            }
    }
}