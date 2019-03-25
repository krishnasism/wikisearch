def search(topic):
    from bs4 import BeautifulSoup
    import requests
    
    response = requests.get("https://en.wikipedia.org/w/index.php?search="+topic+"&title=Special%3ASearch&profile=advanced&fulltext=1")
    soup = BeautifulSoup(response.text,"lxml")
    headings=soup.find_all("div", class_="mw-search-result-heading") #extract all results

    t = soup.find_all("li", class_="mw-search-result") #fetch search results
    

    links=[] #store links in a list
    for i in range(0,len(t)):

        print("OPTION : ")
        print(i) #option number for future reference
        print(headings[i].text) #print headings of the search results
        print(t[i].text) #print the description of the search
        link=t[i].a #extract the <a> </a> tag 

        href="https://www.wikipedia.org"+link['href'] #extract the link
        links.append(href) #append links to list 
        print("-----------------------------------")
        print()

    print("Select option:")
    i=int(input()) 
    
    print("You selected : " +links[i]) 

    #return to calling function
    return (links[i])
       

    
