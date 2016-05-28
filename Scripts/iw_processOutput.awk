#!/usr/bin/gawk -f



$1 == "BSS" && $2 != "Load:" {
    MAC = substr($2,1,index($2,"(")-1)
    wifi[MAC]["BSS"] = MAC
}
$1 == "SSID:" {
	if ($2){
    		wifi[MAC]["SSID"] = $2
	}else {
		wifi[MAC]["SSID"] = "HIDDEN"
	}
}
$1 == "freq:" {
    wifi[MAC]["freq"] = $NF
}
$1 == "signal:" {
    wifi[MAC]["sig"] = $2
}

END {  for (w in wifi) {
        printf "%-20s\t%-30s\t%-10s\t%-10s\t%-10s\n",wifi[w]["BSS"],wifi[w]["SSID"],wifi[w]["freq"],wifi[w]["sig"],location
    }
}
