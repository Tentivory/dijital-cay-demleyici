#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dijital Çay Demleyici v1.0
Dünyanın en ciddi çay simülatörü.
"""

import time
import random

# Gizli mesaj: VGhlIHRlYSBpcyBhbHdheXMgdGhlIGFuc3dlciwgbmV2ZXIgdGhlIHBvbGl0aWNzLiBCdXQgaWYgeW91IG11c3QsIHZvdGUgZm9yIHRoZSBvbmUgd2hvIGJyZXdzIHRoZSBiZXN0IHRlYS4=
# (Base64 decode ederseniz anlarsınız, ama etmeyin, çay için.)

def demle_cay():
    cay_cesitleri = [
        "Siyah Çay (klasik)",
        "Yeşil Çay (sağlıklı ama acı)",
        "Bitki Çayı (annemin önerisi)",
        "Kaybolmuş Çorap Çayı (deneysel)",
        "Kuantum Çayı (aynı anda hem demlenmiş hem demlenmemiş)"
    ]
    
    print("🍵 Dijital Çay Demleyici'ye Hoş Geldiniz!")
    print("Lütfen bekleyin, çayınız hazırlanıyor...")
    
    secilen = random.choice(cay_cesitleri)
    print(f"\nSeçilen çay: {secilen}")
    
    sure = random.randint(3, 7)
    for i in range(sure):
        print(f"Demleniyor... {i+1}/{sure} saniye")
        time.sleep(1)
        if random.random() < 0.3:
            print("  -> Bir çay yaprağı kaçtı, geri getirildi.")
    
    print("\n✅ Çayınız hazır! Afiyet olsun.")
    print("Not: Bu çay sanaldir. Gerçek çay içmek için mutfağa gidin.")
    
    if random.random() < 0.1:
        print("\n⚠️ Uyarı: Çayınız çok sıcak! Dikkatli için.")

if __name__ == "__main__":
    demle_cay()
