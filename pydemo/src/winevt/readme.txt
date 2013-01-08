requirements：

    首先用16进制查看器找到 0x11111111222222223333333344444444 
    將之後16bytes 抄下，這16bytes會在0x28000000前，
    回到檔頭，把這16bytes從第17byte開始 覆寫 到32byte，
    最後在改第37byte的值為 0x08，就可以讀進事件檢視器了。
    
功能描述：
    convert Windows evt file(*.evt) ， so we can import the evt to a new machine.