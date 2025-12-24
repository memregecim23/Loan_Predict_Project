<img width="1621" height="760" alt="image" src="https://github.com/user-attachments/assets/8f92cc40-2c19-4578-b2b8-26a46fa0154f" />
<img width="1487" height="717" alt="image" src="https://github.com/user-attachments/assets/87b9e978-afc9-408d-abe0-76bc3f0bbabb" />
<img width="1831" height="711" alt="image" src="https://github.com/user-attachments/assets/22d25c7e-d6c3-4bf3-9050-6313b34ad8b4" />

Not:Aşağıdaki linke tıklayarak canlı olarak demoyu deneyebilirsiniz.Link aynı zamanda about kısmında da bulunmaktadır.

https://loanpredictproject.streamlit.app/

**Bank Loan Approval Prediction System**
Bu proje, bankacılık sektöründe kredi riskini minimize etmek, batık kredileri (default) önlemek ve kredi onay süreçlerini saniyeler seviyesine indirmek amacıyla geliştirilmiş 
yüksek performanslı bir yapay zeka uygulamasıdır.

**İş Problemi ve Veri Seti Hikayesi**
Bankalar için en büyük finansal risk, krediyi geri ödeyemeyecek müşterilere onay vermektir. Geleneksel yöntemlerde kredi memurları onlarca parametreyi manuel inceler, 
bu da süreci yavaşlatır ve insan hatasına açık hale getirir.

Bu projede kullanılan veri seti, 36 farklı finansal ve demografik değişkeni içerir. Modelimiz, müşterinin sadece gelirine değil; borç oranına (DTI),
harcama alışkanlıklarına, varlıklarına ve geçmiş ödeme performansına bakarak karmaşık bir risk analizi yapar.

**Değişken Açıklamaları**
Modelin karar verirken kullandığı parametreler ve anlamları aşağıdadır;
Değişken Adı,Veri Tipi,Açıklama
ApplicationDate,Object,Kredi başvurusunun yapıldığı tarih (Yıl/Ay/Gün olarak işlenmiştir).
Age,Integer,Müşterinin yaşı.
AnnualIncome,Integer,Yıllık toplam gelir.
CreditScore,Integer,Kredi notu (Fico Score). Finansal güvenilirlik puanı.
EmploymentStatus,Object,"İstihdam durumu (Employed, Self-Employed, Unemployed vb.)."
EducationLevel,Object,"Eğitim seviyesi (Lise, Lisans, Yüksek Lisans, Doktora)."
Experience,Integer,Toplam iş deneyimi (Yıl).
LoanAmount,Integer,Bankadan talep edilen kredi miktarı.
LoanDuration,Integer,Kredinin geri ödeme vadesi (Ay).
MaritalStatus,Object,Medeni durum.
NumberOfDependents,Integer,Bakmakla yükümlü olunan kişi sayısı.
HomeOwnershipStatus,Object,"Ev sahipliği durumu (Kira, Mortgage, Kendi Evi)."
MonthlyDebtPayments,Integer,Müşterinin halihazırda ödediği aylık borç miktarı.
CreditCardUtilizationRate,Float,Kredi kartı limit kullanım oranı (%0 - %100).
NumberOfOpenCreditLines,Integer,Aktif açık kredi hesabı sayısı.
NumberOfCreditInquiries,Integer,Son dönemde yapılan kredi sorgulama sayısı.
DebtToIncomeRatio (DTI),Float,Kritik Metrik: Toplam Borç / Brüt Gelir oranı.
BankruptcyHistory,Integer,"Geçmişte iflas durumu var mı? (1: Evet, 0: Hayır)."
LoanPurpose,Object,"Kredinin kullanım amacı (Eğitim, Araba, Ev, Borç Kapama)."
PreviousLoanDefaults,Integer,"Daha önce batık kredisi var mı? (1: Evet, 0: Hayır)."
PaymentHistory,Integer,Ödeme performans puanı.
LengthOfCreditHistory,Integer,Kredi geçmişinin uzunluğu (Yıl).
SavingsAccountBalance,Integer,Tasarruf hesabındaki bakiye.
CheckingAccountBalance,Integer,Vadesiz hesaptaki bakiye.
TotalAssets,Integer,Toplam varlıklar (Menkul + Gayrimenkul).
TotalLiabilities,Integer,Toplam yükümlülükler (Borçlar).
MonthlyIncome,Float,Aylık net gelir.
UtilityBillsPaymentHistory,Float,Faturaları zamanında ödeme oranı.
JobTenure,Integer,Mevcut işteki çalışma süresi (Yıl).
NetWorth,Integer,Net servet (Varlıklar - Borçlar).
BaseInterestRate,Float,Piyasa baz faiz oranı.
InterestRate,Float,Müşteriye uygulanan faiz oranı.
MonthlyLoanPayment,Float,Bu kredi için hesaplanan aylık taksit.
TotalDebtToIncomeRatio,Float,Tüm borçların gelire oranı.
RiskScore,Float,Banka içi hesaplanan risk skoru.
LoanApproved,Integer,"HEDEF DEĞİŞKEN: Kredi Onaylandı mı? (1: Onay, 0: Red)."


**Model Mimarisi**
Bu projede, tabular verilerde en iyi performansı veren ve RandomizedSearchCV ile hiperparametreleri optimize edilmiş LightGBM (LGBMClassifier) kullanılmıştır.
- Algoritma: LightGBM (Gradient Boosting Framework)
- Optimizasyon: RandomizedSearchCV kullanılarak n_estimators, learning_rate ve max_depth gibi parametreler optimize edilmiştir.
- Dengesiz Veri Yönetimi: is_unbalance=True parametresi ile kredi onay/red oranlarındaki dengesizlik (Class Imbalance) yönetilmiştir.

### Model Performans Sonuçları

Yapılan iyileştirmeler ve hiperparametre optimizasyonu sonucunda modelin başarısı **%95** seviyesine ulaşmıştır.

#### 1. Confusion Matrix
| Gerçek \ Tahmin | 0 (Negatif) | 1 (Pozitif) |
| :--- | :---: | :---: |
| **0** | 4289 | 233 |
| **1** | 88 | 1390 |

#### 2. Sınıflandırma Raporu
| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **0** | 0.98 | 0.95 | 0.96 | 4522 |
| **1** | 0.86 | 0.94 | 0.90 | 1478 |
| **Accuracy** | | | **0.95** | **6000** |
| **Macro Avg** | 0.92 | 0.94 | 0.93 | 6000 |
| **Weighted Avg**| 0.95 | 0.95 | 0.95 | 6000 |

**Genel Doğruluk (Accuracy):** `%95.11`

  Kütüphaneleri Yükleyin:
**pip install -r requirements.txt**
Uygulamayı Başlatın: Terminali (veya CMD'yi) proje klasöründe açın ve şu kodu çalıştırın:
**streamlit run app2.py**
(Tarayıcınızda otomatik olarak interaktif arayüz açılacaktır.)

Geliştirici:Mustafa Emre Geçim
