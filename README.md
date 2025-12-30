<img width="1621" height="760" alt="image" src="https://github.com/user-attachments/assets/8f92cc40-2c19-4578-b2b8-26a46fa0154f" />
<img width="1487" height="717" alt="image" src="https://github.com/user-attachments/assets/87b9e978-afc9-408d-abe0-76bc3f0bbabb" />
<img width="1831" height="711" alt="image" src="https://github.com/user-attachments/assets/22d25c7e-d6c3-4bf3-9050-6313b34ad8b4" />

Not:Aşağıdaki linke tıklayarak canlı olarak demoyu deneyebilirsiniz.Link aynı zamanda about kısmında da bulunmaktadır.Uygulama için gerekli olan csv dosyası repodadır.

https://loanpredictproject.streamlit.app/

# Bank Loan Approval Prediction System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-LightGBM-green)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Proje Özeti
Bu proje, bankacılık sektöründe kredi riskini minimize etmek, batık kredileri (default) önlemek ve kredi onay süreçlerini saniyeler seviyesine indirmek amacıyla geliştirilmiş yüksek performanslı bir yapay zeka uygulamasıdır. 

Model, 36 farklı finansal ve demografik değişkeni analiz ederek müşterinin risk profilini çıkarır ve kredi onayı için karar desteği sunar.

## İş Problemi
Bankalar için en büyük finansal risk, krediyi geri ödeyemeyecek müşterilere onay vermektir. Geleneksel yöntemlerde:
* Kredi memurları onlarca parametreyi manuel inceler.
* Süreç yavaştır ve maliyetlidir.
* İnsan hatasına ve subjektif kararlara açıktır.

**Çözüm:** Müşterinin sadece gelirine değil; borç oranına (DTI), harcama alışkanlıklarına, varlıklarına ve geçmiş ödeme performansına bakarak karmaşık bir risk analizi yapan otomatik bir model geliştirmek.

## Veri Seti Hikayesi ve Değişkenler
Veri seti, finansal geçmişi ve demografik bilgileri içeren **36 değişkenden** oluşmaktadır.

| Değişken Adı | Veri Tipi | Açıklama |
| :--- | :--- | :--- |
| **LoanApproved** | Integer | **HEDEF DEĞİŞKEN:** Kredi Onaylandı mı? (1: Onay, 0: Red) |
| `ApplicationDate` | Object | Başvuru tarihi (Yıl/Ay/Gün). |
| `Age` | Integer | Müşterinin yaşı. |
| `AnnualIncome` | Integer | Yıllık toplam gelir. |
| `CreditScore` | Integer | Kredi notu (Fico Score). |
| `EmploymentStatus` | Object | İstihdam durumu (Employed, Self-Employed vb.). |
| `EducationLevel` | Object | Eğitim seviyesi. |
| `Experience` | Integer | Toplam iş deneyimi (Yıl). |
| `LoanAmount` | Integer | Talep edilen kredi miktarı. |
| `LoanDuration` | Integer | Geri ödeme vadesi (Ay). |
| `MaritalStatus` | Object | Medeni durum. |
| `NumberOfDependents` | Integer | Bakmakla yükümlü olunan kişi sayısı. |
| `HomeOwnershipStatus` | Object | Ev sahipliği durumu. |
| `MonthlyDebtPayments` | Integer | Halihazırda ödenen aylık borç miktarı. |
| `CreditCardUtilizationRate` | Float | Kredi kartı limit kullanım oranı. |
| `NumberOfOpenCreditLines` | Integer | Aktif açık kredi hesabı sayısı. |
| `NumberOfCreditInquiries` | Integer | Son dönemde yapılan kredi sorgulama sayısı. |
| `DebtToIncomeRatio (DTI)` | Float | **Kritik Metrik:** Toplam Borç / Brüt Gelir oranı. |
| `BankruptcyHistory` | Integer | Geçmişte iflas durumu (1: Evet, 0: Hayır). |
| `LoanPurpose` | Object | Kredinin kullanım amacı. |
| `PreviousLoanDefaults` | Integer | Daha önce batık kredisi var mı? |
| `PaymentHistory` | Integer | Ödeme performans puanı. |
| `LengthOfCreditHistory` | Integer | Kredi geçmişinin uzunluğu (Yıl). |
| `SavingsAccountBalance` | Integer | Tasarruf hesabındaki bakiye. |
| `CheckingAccountBalance` | Integer | Vadesiz hesaptaki bakiye. |
| `TotalAssets` | Integer | Toplam varlıklar. |
| `TotalLiabilities` | Integer | Toplam yükümlülükler. |
| `MonthlyIncome` | Float | Aylık net gelir. |
| `UtilityBillsPaymentHistory` | Float | Faturaları zamanında ödeme oranı. |
| `JobTenure` | Integer | Mevcut işteki çalışma süresi (Yıl). |
| `NetWorth` | Integer | Net servet (Varlıklar - Borçlar). |
| `BaseInterestRate` | Float | Piyasa baz faiz oranı. |
| `InterestRate` | Float | Müşteriye uygulanan faiz oranı. |
| `MonthlyLoanPayment` | Float | Hesaplanan aylık taksit. |
| `TotalDebtToIncomeRatio` | Float | Tüm borçların gelire oranı. |
| `RiskScore` | Float | Banka içi hesaplanan risk skoru. |

## Model Mimarisi
Projede, tabular verilerde en yüksek performansı gösteren Gradient Boosting algoritmalarından **LightGBM** tercih edilmiştir.

* **Algoritma:** LightGBM (LGBMClassifier)
* **Optimizasyon:** `RandomizedSearchCV` kullanılarak hiperparametre optimizasyonu yapılmıştır.
    * *Optimize edilen parametreler:* `n_estimators`, `learning_rate`, `max_depth`.
* **Dengesiz Veri Yönetimi:** Finansal verilerde sınıf dengesizliğini yönetmek için `is_unbalance=True` parametresi kullanılmıştır.

## Model Performansı
Yapılan iyileştirmeler ve hiperparametre optimizasyonu sonucunda modelin genel başarısı **%95.11** seviyesine ulaşmıştır.

### 1. Confusion Matrix (Karmaşıklık Matrisi)
| Gerçek \ Tahmin | 0 (Negatif - Red) | 1 (Pozitif - Onay) |
| :--- | :---: | :---: |
| **0** | 4289 | 233 |
| **1** | 88 | 1390 |

### 2. Sınıflandırma Raporu (Classification Report)
| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **0** | 0.98 | 0.95 | 0.96 | 4522 |
| **1** | 0.86 | 0.94 | 0.90 | 1478 |
| **Accuracy** | | | **0.95** | **6000** |
| **Macro Avg** | 0.92 | 0.94 | 0.93 | 6000 |
| **Weighted Avg**| 0.95 | 0.95 | 0.95 | 6000 |

> **Genel Doğruluk (Accuracy):** `%95.11`

## Kurulum ve Kullanım

Projeyi yerel ortamınızda çalıştırmak ve arayüzü görmek için:

1.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Uygulamayı Başlatın:**
    Terminali proje klasöründe açın ve Streamlit arayüzünü başlatın:
    ```bash
    streamlit run app2.py
    ```
    *(Tarayıcınızda otomatik olarak interaktif arayüz açılacaktır.)*

---
*Geliştirici: **Mustafa Emre Geçim***
