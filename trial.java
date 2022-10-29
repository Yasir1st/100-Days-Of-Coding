/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package trialJava;
import java.util.Scanner;

public class trial {
    public static void main(String[] args) {
        String namaDepan, namaBelakang, noTelp;
        float  tinggi;
        double beratBadan;
        int    umur;
        boolean statusNikah;
        
        Scanner Scan = new Scanner(System.in);
        
        space();
        System.out.println("                Data Diri");
        space();
        System.out.print("Masukkan Nama Depan : ");
        namaDepan = Scan.nextLine();
        System.out.print("Masukkan Nama Belakang : ");
        namaBelakang = Scan.nextLine();
        System.out.print("Masukkan No Telp : ");
        noTelp = Scan.nextLine();
        System.out.print("Masukkan Tinggi Dadan : ");
        tinggi = Scan.nextFloat();
        System.out.print("Masukkan Berat Badan : ");
        beratBadan = Scan.nextDouble();
        System.out.print("Masukkan Umur : ");
        umur = Scan.nextInt();
        System.out.print("Masukkan Status Pernikahan(true/false) : ");
        statusNikah = Scan.nextBoolean();
        space();
        // Output
        System.out.println("Nama Depan : "+namaDepan);
        System.out.println("Nama Belakang : "+namaBelakang);
        System.out.println("No Telpon : "+noTelp);
        System.out.println("Tinggi Badan : "+tinggi+" cm");
        System.out.println("Berat Badan : "+beratBadan+" kg");
        System.out.println("Umur : "+umur);
        
        if(statusNikah == true){
            System.out.println("Status Pernikahan : Sudah Menikah");  
        }else{
            System.out.println("Status Pernikahan : Blum Menikah");
        }
        space();
    }
    public static void space(){
        System.out.println("=======================================");
        return;
    }
}
