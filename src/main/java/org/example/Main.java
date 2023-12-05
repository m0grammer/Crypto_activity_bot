package org.example;

import org.jsoup.*;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) throws IOException {
        Document doc = Jsoup.connect("https://coinmarketcap.com/").get();
        Elements prices = doc.getElementsByClass("sc-a0353bbc-0 gDrtaY");
        Elements names = doc.getElementsByClass("sc-adbfcfff-3 dDrhas");
        List<String> cryptoNames = new ArrayList<>();
        List<String> cryptoPrice = new ArrayList<>();
        for (Element name: names) {
            cryptoNames.add(name.text());
        }
        for (Element price:prices) {
            cryptoPrice.add(price.text());
        }

        try {
            for (int i=0; i < cryptoNames.size(); i++){
                System.out.println("Name: " + cryptoNames.get(i) + " | " + "Price: " + cryptoPrice.get(i));
            }
        } catch (Exception e){
            System.out.println("Error: " + e);
        }
    }
}
