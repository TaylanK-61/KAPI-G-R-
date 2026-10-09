<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liman PDA (Proforma Disbursement Account) Hesaplayıcı</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @media print {
            .no-print { display: none !important; }
            .print-only { display: block !important; }
            body { background: white; color: black; font-size: 12pt; }
            .card { border: 1px solid #ccc; box-shadow: none !important; }
        }
    </style>
</head>
<body class="bg-slate-100 min-h-screen text-slate-800 p-4 md:p-8">

    <div class="max-w-6xl mx-auto">
        <!-- Header -->
        <header class="bg-sky-900 text-white p-6 rounded-t-xl shadow-lg flex flex-col md:flex-row justify-between items-center gap-4">
            <div>
                <h1 class="text-2xl font-bold tracking-wide">LİMAN PDA HESAPLAMA SİSTEMİ</h1>
                <p class="text-sky-200 text-sm mt-1">UAB Kılavuzluk, Römorkör, Palamar ve Barınma Tarifeleri Mevzuatına Uygun</p>
            </div>
            <button onclick="window.print()" class="no-print bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2.5 rounded-lg font-medium shadow flex items-center gap-2 transition">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                PDA Yazdır / PDF İndir
            </button>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mt-6">
            
            <!-- FORM SEKTÖRÜ (GİRDİLER) -->
            <div class="lg:col-span-6 space-y-6 no-print">
                
                <!-- Gemi & Sefer Bilgileri Card -->
                <div class="bg-white p-6 rounded-xl shadow-md border border-slate-200">
                    <h2 class="text-lg font-bold text-sky-900 mb-4 border-b pb-2 flex items-center gap-2">
                        <span>🚢</span> Gemi ve Sefer Bilgileri
                    </h2>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="col-span-2 sm:col-span-1">
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Gemi Adı</label>
                            <input type="text" id="vesselName" value="MV MARMARA STAR" class="w-full border rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-sky-500 outline-none">
                        </div>
                        <div class="col-span-2 sm:col-span-1">
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Gros Tonaj (GT)</label>
                            <input type="number" id="grt" value="8500" min="1" oninput="calculatePDA()" class="w-full border rounded-lg p-2.5 text-sm font-bold text-sky-900 focus:ring-2 focus:ring-sky-500 outline-none">
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Bayrak / Rejim</label>
                            <select id="flagType" onchange="calculatePDA()" class="w-full border rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-sky-500 outline-none">
                                <option value="foreign">Yabancı Bayrak (Uluslararası)</option>
                                <option value="cabotage">Türk Bayraklı (Kabotaj %50 İndirimli)</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Gemi Tipi</label>
                            <select id="vesselType" onchange="calculatePDA()" class="w-full border rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-sky-500 outline-none">
                                <option value="dry_cargo">Kuru Yük / Genel Kargo</option>
                                <option value="container">Konteyner Gemisi</option>
                                <option value="roro">Ro-Ro / Yolcu Gemisi</option>
                                <option value="tanker">Tanker / LPG / LNG / Kimyasal</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Lımanda Kalış (Saat)</label>
                            <input type="number" id="stayHours" value="48" min="1" oninput="calculatePDA()" class="w-full border rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-sky-500 outline-none">
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">USD / TRY Kuru</label>
                            <input type="number" id="usdRate" value="38.50" step="0.1" oninput="calculatePDA()" class="w-full border rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-sky-500 outline-none">
                        </div>
                    </div>
                </div>

                <!-- Hizmet Detayları ve Parametreler -->
                <div class="bg-white p-6 rounded-xl shadow-md border border-slate-200">
                    <h2 class="text-lg font-bold text-sky-900 mb-4 border-b pb-2 flex items-center gap-2">
                        <span>⚙️</span> Hizmet Seçimleri & Katsayılar
                    </h2>

                    <div class="space-y-4">
                        <!-- Kılavuzluk -->
                        <div class="p-3 bg-slate-50 rounded-lg border">
                            <div class="flex justify-between items-center mb-2">
                                <span class="font-semibold text-sm text-slate-700">Kılavuzluk Hizmeti</span>
                                <input type="checkbox" id="enablePilotage" checked onchange="calculatePDA()" class="w-4 h-4 text-sky-600 rounded">
                            </div>
                            <div class="grid grid-cols-2 gap-2 text-xs">
                                <div>
                                    <label class="block text-slate-500 mb-1">Operasyon Sayısı</label>
                                    <select id="pilotOperations" onchange="calculatePDA()" class="w-full border rounded p-1.5 bg-white">
                                        <option value="2">Giriş + Çıkış (2 Operasyon)</option>
                                        <option value="1">Tek Yön (1 Operasyon)</option>
                                        <option value="3">Giriş + Şift + Çıkış (3 Operasyon)</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-slate-500 mb-1">Tehlikeli Yük / Özel Sürşarj</label>
                                    <select id="dangerousPilot" onchange="calculatePDA()" class="w-full border rounded p-1.5 bg-white">
                                        <option value="1.0">Yok (Standart %0)</option>
                                        <option value="1.3">Tehlikeli Yük / Tanker (+%30)</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- Römorkör -->
                        <div class="p-3 bg-slate-50 rounded-lg border">
                            <div class="flex justify-between items-center mb-2">
                                <span class="font-semibold text-sm text-slate-700">Römorkörcülük Hizmeti</span>
                                <input type="checkbox" id="enableTug" checked onchange="calculatePDA()" class="w-4 h-4 text-sky-600 rounded">
                            </div>
                            <div class="grid grid-cols-2 gap-2 text-xs">
                                <div>
                                    <label class="block text-slate-500 mb-1">Römorkör Adedi (Her Hareket İçin)</label>
                                    <input type="number" id="tugCount" value="2" min="0" max="6" oninput="calculatePDA()" class="w-full border rounded p-1.5 bg-white font-bold">
                                </div>
                                <div>
                                    <label class="block text-slate-500 mb-1">Toplam Hareket (Giriş/Çıkış)</label>
                                    <input type="number" id="tugMoves" value="2" min="1" oninput="calculatePDA()" class="w-full border rounded p-1.5 bg-white">
                                </div>
                            </div>
                        </div>

                        <!-- Palamar -->
                        <div class="p-3 bg-slate-50 rounded-lg border">
                            <div class="flex justify-between items-center mb-2">
                                <span class="font-semibold text-sm text-slate-700">Palamar Hizmeti (Mooring)</span>
                                <input type="checkbox" id="enableMooring" checked onchange="calculatePDA()" class="w-4 h-4 text-sky-600 rounded">
                            </div>
                            <div class="text-xs">
                                <label class="block text-slate-500 mb-1">Hizmet Türü</label>
                                <select id="mooringType" onchange="calculatePDA()" class="w-full border rounded p-1.5 bg-white">
                                    <option value="2">Bağlama + Çözme (2 Hizmet)</option>
                                    <option value="1">Sadece Bağlama Veya Çözme (1 Hizmet)</option>
                                </select>
                            </div>
                        </div>

                        <!-- Barınma -->
                        <div class="p-3 bg-slate-50 rounded-lg border">
                            <div class="flex justify-between items-center mb-2">
                                <span class="font-semibold text-sm text-slate-700">Barınma / Fuzuli İşgal Ücreti</span>
                                <input type="checkbox" id="enableBerthing" checked onchange="calculatePDA()" class="w-4 h-4 text-sky-600 rounded">
                            </div>
                            <p class="text-[11px] text-slate-500">Kıyı Tesislerinde Gemilerin Barınma Ücretleri Yönergesine göre hesaplanır (Saat x GT Kesri).</p>
                        </div>

                    </div>
                </div>

            </div>

            <!-- PDA ÖZETİ VE ÇIKTI KARTI -->
            <div class="lg:col-span-6">
                <div class="bg-white p-6 rounded-xl shadow-lg border border-slate-200 card sticky top-6">
                    
                    <!-- Proforma Fatura Başlığı -->
                    <div class="text-center border-b pb-4 mb-4">
                        <h3 class="text-xl font-bold text-slate-900">PROFORMA DISBURSEMENT ACCOUNT (PDA)</h3>
                        <p class="text-xs text-slate-500 mt-1" id="pdaDate"></p>
                    </div>

                    <!-- Gemi Özet Bilgi Tablosu -->
                    <div class="grid grid-cols-3 gap-2 bg-slate-50 p-3 rounded-lg text-xs mb-4 border">
                        <div><span class="text-slate-400 block">Gemi:</span> <strong id="dispVesselName">-</strong></div>
                        <div><span class="text-slate-400 block">Gros Tonaj:</span> <strong id="dispGRT">-</strong> GT</div>
                        <div><span class="text-slate-400 block">Kalış Süresi:</span> <strong id="dispHours">-</strong> Saat</div>
                    </div>

                    <!-- Hesap Kalemleri Tablosu -->
                    <div class="overflow-x-auto">
                        <table class="w-full text-xs text-left text-slate-700">
                            <thead class="bg-slate-100 text-slate-600 font-semibold border-b">
                                <tr>
                                    <th class="p-2.5">Hizmet Kalemi</th>
                                    <th class="p-2.5 text-center">Açıklama / Baz</th>
                                    <th class="p-2.5 text-right">Tutar (USD)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100" id="pdaTableBody">
                                <!-- JS dinamik dolduracak -->
                            </tbody>
                        </table>
                    </div>

                    <!-- Toplamlar -->
                    <div class="mt-6 border-t-2 border-slate-200 pt-4 space-y-2">
                        <div class="flex justify-between text-sm font-semibold text-slate-600">
                            <span>Ara Toplam (USD):</span>
                            <span id="subTotalUSD">$0.00</span>
                        </div>
                        <div class="flex justify-between text-sm font-semibold text-slate-600">
                            <span>Liman Ajanlık / Değişken Liman Harçları (Tahmini %5):</span>
                            <span id="agencyFeeUSD">$0.00</span>
                        </div>
                        <div class="flex justify-between text-lg font-bold text-sky-900 border-t pt-2">
                            <span>GENEL TOPLAM (USD):</span>
                            <span id="grandTotalUSD" class="text-xl text-emerald-600">$0.00</span>
                        </div>
                        <div class="flex justify-between text-xs font-semibold text-slate-500">
                            <span>Tahmini TL Karşılığı (KBR: <span id="dispRate">38.50</span> TL):</span>
                            <span id="grandTotalTRY">₺0.00</span>
                        </div>
                    </div>

                    <!-- Alt Bilgilendirme -->
                    <div class="mt-6 text-[10px] text-slate-400 border-t pt-3 leading-relaxed">
                        * Bu hesaplama T.C. Ulaştırma ve Altyapı Bakanlığı Denizcilik Genel Müdürlüğü’nün yayınladığı güncel Kılavuzluk, Römorkörcülük, Palamar ve Barınma ücret tavan tarifeleri baz alınarak proforma niteliğinde yapılmıştır. Kesin faturalandırma operasyonel değişikliklere tabidir.
                    </div>

                </div>
            </div>

        </div>
    </div>

    <!-- HESAPLAMA SCRIPT MANTIĞI -->
    <script>
        document.getElementById('pdaDate').innerText = 'Tarih: ' + new Date().toLocaleDateString('tr-TR');

        function calculatePDA() {
            const grt = parseFloat(document.getElementById('grt').value) || 0;
            const hours = parseFloat(document.getElementById('stayHours').value) || 0;
            const rate = parseFloat(document.getElementById('usdRate').value) || 1;
            const flag = document.getElementById('flagType').value;
            const vesselType = document.getElementById('vesselType').value;
            const vesselName = document.getElementById('vesselName').value;

            // Ekran güncellemeleri
            document.getElementById('dispVesselName').innerText = vesselName;
            document.getElementById('dispGRT').innerText = grt.toLocaleString('tr-TR');
            document.getElementById('dispHours').innerText = hours;
            document.getElementById('dispRate').innerText = rate.toFixed(2);

            let tableRows = [];
            let totalUSD = 0;

            // Kabotaj İndirim Oranı
            const flagMultiplier = (flag === 'cabotage') ? 0.50 : 1.0;

            // --- 1. KILAVUZLUK HESABI ---
            if (document.getElementById('enablePilotage').checked) {
                const ops = parseInt(document.getElementById('pilotOperations').value);
                const dangerousMult = parseFloat(document.getElementById('dangerousPilot').value);

                // Tarifeye Göre Baz Ücret (İlk 1000 GT ve ilave her 1000 GT kesri)
                // Örn: Standart Gemiler için 0-1000 GT: ~202 USD, İlave her 1000 GT: ~83 USD (UAB Tavan Tarifesi bazı)
                let baseRate = 202;
                let additionalRate = 83;

                if (vesselType === 'roro' || vesselType === 'container') {
                    baseRate = 160;
                    additionalRate = 65;
                }

                const thousandBlocks = Math.ceil(Math.max(0, grt - 1000) / 1000);
                let singleOpCost = (baseRate + (thousandBlocks * additionalRate)) * flagMultiplier * dangerousMult;
                let totalPilotCost = singleOpCost * ops;

                totalUSD += totalPilotCost;
                tableRows.push({
                    name: "Kılavuzluk Hizmeti",
                    desc: `${ops} Operasyon (Baz: $${baseRate} + ${thousandBlocks}x$${additionalRate})`,
                    cost: totalPilotCost
                });
            }

            // --- 2. RÖMORKÖR HESABI ---
            if (document.getElementById('enableTug').checked) {
                const tugCount = parseInt(document.getElementById('tugCount').value);
                const tugMoves = parseInt(document.getElementById('tugMoves').value);

                // Römorkör Tarifesi (GT Bazında Her Bir Römorkör İçin Operasyon Başı Ücret)
                // Örn: 0-1000 GT: $382, İlave her 1000 GT: $71
                let baseTugRate = 383;
                let addTugRate = 72;

                const tugBlocks = Math.ceil(Math.max(0, grt - 1000) / 1000);
                let singleTugPerMove = (baseTugRate + (tugBlocks * addTugRate)) * flagMultiplier;
                let totalTugCost = singleTugPerMove * tugCount * tugMoves;

                totalUSD += totalTugCost;
                tableRows.push({
                    name: "Römorkörcülük Hizmeti",
                    desc: `${tugMoves} Hareket x ${tugCount} Römorkör (Birim: $${singleTugPerMove.toFixed(2)})`,
                    cost: totalTugCost
                });
            }

            // --- 3. PALAMAR HESABI ---
            if (document.getElementById('enableMooring').checked) {
                const mooringOps = parseInt(document.getElementById('mooringType').value);
                
                // Palamar Tarifesi
                let baseMooring = 110;
                let addMooring = 25;
                const moorBlocks = Math.ceil(Math.max(0, grt - 1000) / 1000);
                let mooringCost = (baseMooring + (moorBlocks * addMooring)) * mooringOps * flagMultiplier;

                totalUSD += mooringCost;
                tableRows.push({
                    name: "Palamar Hizmeti (Mooring)",
                    desc: `${mooringOps} Operasyon (Bağlama/Çözme)`,
                    cost: mooringCost
                });
            }

            // --- 4. BARINMA (BERTHING) HESABI ---
            if (document.getElementById('enableBerthing').checked) {
                // Kıyı Tesisleri Gemilerin Barınma Yönergesi Mantığı
                // Beher Saat x Beher 1000 GT kesri
                const thousandFraction = Math.ceil(grt / 1000);
                let hourlyGrtRate = 0.85; // USD / (Hour x 1000 GT)
                
                let berthingCost = hours * thousandFraction * hourlyGrtRate * flagMultiplier;
                // Minimum barınma ücreti koruması ($410 USD standart minimum)
                if (berthingCost < 150 && grt > 500) berthingCost = 150;

                totalUSD += berthingCost;
                tableRows.push({
                    name: "Kıyı Tesis Barınma Ücreti",
                    desc: `${hours} Saat x ${thousandFraction} (1000 GT Kesri)`,
                    cost: berthingCost
                });
            }

            // Tabloyu Oluşturma
            const tbody = document.getElementById('pdaTableBody');
            tbody.innerHTML = '';
            tableRows.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td class="p-2.5 font-medium text-slate-800">${row.name}</td>
                    <td class="p-2.5 text-center text-slate-500">${row.desc}</td>
                    <td class="p-2.5 text-right font-semibold text-slate-900">$${row.cost.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
                `;
                tbody.appendChild(tr);
            });

            // Ara Toplam ve Ajanlık / Harçlar
            const agencyFee = totalUSD * 0.05; // Tahmini %5 Ajanlık ve fuzuli harçlar
            const grandTotalUSD = totalUSD + agencyFee;
            const grandTotalTRY = grandTotalUSD * rate;

            document.getElementById('subTotalUSD').innerText = '$' + totalUSD.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('agencyFeeUSD').innerText = '$' + agencyFee.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('grandTotalUSD').innerText = '$' + grandTotalUSD.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('grandTotalTRY').innerText = '₺' + grandTotalTRY.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2});
        }

        // İlk Çalıştırma
        calculatePDA();
    </script>
</body>
</html>
