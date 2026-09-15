// Dashboard Controller Application for CIER Survey

document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initCharts();
  renderIndicesTable();
  renderSatisfactionTable();
  renderBenchmark500kTable();
  renderDictionaryTable();
  renderFilesGrid();
  initFilters();
});

// 1. Tab Navigation Controller
function initTabs() {
  const tabs = document.querySelectorAll('.nav-tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const targetPanel = document.getElementById(tab.getAttribute('data-tab'));
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });
}

// 2. Chart.js Visualizations (Radar Charts & Benchmark Analysis)
function initCharts() {
  if (typeof Chart === 'undefined') return;

  // Chart 1: Radar Chart - 5 Areas of Quality (IDAR)
  const ctxAreas = document.getElementById('chart-areas');
  if (ctxAreas) {
    new Chart(ctxAreas.getContext('2d'), {
      type: 'radar',
      data: {
        labels: [
          'Suministro (SE)', 
          'Factura (FE)', 
          'Atención (AT)', 
          'Imagen (IM)', 
          'Información (IC)',
          'Resp. Socioamb. (RSA)'
        ],
        datasets: [
          {
            label: 'Año 2025',
            data: [75.79, 70.21, 66.63, 56.54, 46.46, 55.34],
            backgroundColor: 'rgba(59, 130, 246, 0.22)',
            borderColor: 'rgba(96, 165, 250, 1)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(96, 165, 250, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 4,
            pointHoverRadius: 7
          },
          {
            label: 'Año 2026',
            data: [78.48, 70.38, 68.10, 60.53, 52.03, 59.57],
            backgroundColor: 'rgba(6, 182, 212, 0.32)',
            borderColor: 'rgba(34, 211, 238, 1)',
            borderWidth: 2.5,
            pointBackgroundColor: 'rgba(34, 211, 238, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 5,
            pointHoverRadius: 8
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        elements: {
          line: { tension: 0.15 }
        },
        plugins: {
          legend: {
            position: 'top',
            labels: {
              color: '#f3f4f6',
              font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' },
              padding: 16,
              usePointStyle: true,
              pointStyle: 'circle'
            }
          },
          tooltip: {
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            titleFont: { family: 'Plus Jakarta Sans', size: 13, weight: '700' },
            bodyFont: { family: 'Plus Jakarta Sans', size: 12 },
            padding: 12,
            borderColor: 'rgba(255, 255, 255, 0.1)',
            borderWidth: 1,
            callbacks: {
              label: (item) => ` ${item.dataset.label}: ${item.raw.toFixed(2)} pts`
            }
          }
        },
        scales: {
          r: {
            angleLines: { color: 'rgba(255, 255, 255, 0.12)' },
            grid: { color: 'rgba(255, 255, 255, 0.08)' },
            pointLabels: {
              color: '#e5e7eb',
              font: { family: 'Plus Jakarta Sans', size: 11.5, weight: '600' },
              padding: 10
            },
            ticks: {
              color: '#9ca3af',
              backdropColor: 'transparent',
              stepSize: 15,
              font: { size: 10 }
            },
            suggestedMin: 35,
            suggestedMax: 85
          }
        }
      }
    });
  }

  // Chart 2: Radar Chart - Global Benchmark Indices
  const ctxGlobal = document.getElementById('chart-global');
  if (ctxGlobal) {
    new Chart(ctxGlobal.getContext('2d'), {
      type: 'radar',
      data: {
        labels: [
          'Aprobación (IAC)',
          'ISCAL Global',
          'Intermedio (IIS)',
          'Satisfacción Gen. (ISG)',
          'Excelencia (IECP)',
          'Insatisfacción (IICP)'
        ],
        datasets: [
          {
            label: 'Año 2025',
            data: [75.68, 63.69, 70.24, 61.12, 21.61, 17.66],
            backgroundColor: 'rgba(139, 92, 246, 0.22)',
            borderColor: 'rgba(167, 139, 250, 1)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(167, 139, 250, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 4,
            pointHoverRadius: 7
          },
          {
            label: 'Año 2026',
            data: [77.60, 65.96, 77.56, 65.60, 27.15, 15.19],
            backgroundColor: 'rgba(16, 185, 129, 0.32)',
            borderColor: 'rgba(52, 211, 153, 1)',
            borderWidth: 2.5,
            pointBackgroundColor: 'rgba(52, 211, 153, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 5,
            pointHoverRadius: 8
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        elements: {
          line: { tension: 0.15 }
        },
        plugins: {
          legend: {
            position: 'top',
            labels: {
              color: '#f3f4f6',
              font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' },
              padding: 16,
              usePointStyle: true,
              pointStyle: 'circle'
            }
          },
          tooltip: {
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            titleFont: { family: 'Plus Jakarta Sans', size: 13, weight: '700' },
            bodyFont: { family: 'Plus Jakarta Sans', size: 12 },
            padding: 12,
            borderColor: 'rgba(255, 255, 255, 0.1)',
            borderWidth: 1,
            callbacks: {
              label: (item) => ` ${item.dataset.label}: ${item.raw.toFixed(2)} pts`
            }
          }
        },
        scales: {
          r: {
            angleLines: { color: 'rgba(255, 255, 255, 0.12)' },
            grid: { color: 'rgba(255, 255, 255, 0.08)' },
            pointLabels: {
              color: '#e5e7eb',
              font: { family: 'Plus Jakarta Sans', size: 11.5, weight: '600' },
              padding: 10
            },
            ticks: {
              color: '#9ca3af',
              backdropColor: 'transparent',
              stepSize: 20,
              font: { size: 10 }
            },
            suggestedMin: 0,
            suggestedMax: 90
          }
        }
      }
    });
  }

  // Chart 3: Benchmark Radar Chart - EPEC vs Promedio >500k vs Líder >500k (2026)
  const ctxRadar500k = document.getElementById('chart-radar-500k');
  if (ctxRadar500k) {
    new Chart(ctxRadar500k.getContext('2d'), {
      type: 'radar',
      data: {
        labels: [
          'Suministro (SE)',
          'Sin Interrupción',
          'Sin Variación Voltaje',
          'Facturación (FE)',
          'Facilidad Pago',
          'Atención (AT)',
          'Calidad Atención',
          'Información (IC)',
          'Imagen (IM)',
          'Medio Ambiente',
          'Resp. Socioamb. (RSA)',
          'ISCAL Global'
        ],
        datasets: [
          {
            label: 'EPEC 2026',
            data: [78.48, 85.92, 77.40, 70.38, 89.20, 68.10, 77.63, 52.03, 60.53, 63.46, 59.57, 65.96],
            backgroundColor: 'rgba(6, 182, 212, 0.35)',
            borderColor: 'rgba(34, 211, 238, 1)',
            borderWidth: 2.5,
            pointBackgroundColor: 'rgba(34, 211, 238, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 5,
            pointHoverRadius: 8
          },
          {
            label: 'Promedio >500k (2026)',
            data: [77.80, 84.30, 76.20, 72.40, 88.10, 70.50, 78.10, 57.40, 63.80, 63.20, 60.90, 70.15],
            backgroundColor: 'rgba(59, 130, 246, 0.20)',
            borderColor: 'rgba(96, 165, 250, 1)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(96, 165, 250, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 4,
            pointHoverRadius: 7
          },
          {
            label: 'Benchmark Líder >500k (2026)',
            data: [88.50, 93.40, 87.20, 82.60, 95.80, 83.40, 89.10, 71.30, 79.40, 80.50, 76.80, 83.10],
            backgroundColor: 'rgba(245, 158, 11, 0.12)',
            borderColor: 'rgba(251, 191, 36, 1)',
            borderWidth: 2,
            borderDash: [5, 5],
            pointBackgroundColor: 'rgba(251, 191, 36, 1)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1.5,
            pointRadius: 4,
            pointHoverRadius: 7
          },
          {
            label: 'EPEC 2025 (Histórico)',
            data: [75.79, 83.52, 73.40, 70.21, 87.40, 66.63, 75.20, 46.46, 56.54, 56.31, 55.34, 63.69],
            backgroundColor: 'rgba(139, 92, 246, 0.08)',
            borderColor: 'rgba(167, 139, 250, 0.7)',
            borderWidth: 1.5,
            borderDash: [3, 3],
            pointBackgroundColor: 'rgba(167, 139, 250, 0.7)',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1,
            pointRadius: 3,
            pointHoverRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        elements: {
          line: { tension: 0.15 }
        },
        plugins: {
          legend: {
            position: 'top',
            labels: {
              color: '#f3f4f6',
              font: { family: 'Plus Jakarta Sans', size: 11.5, weight: '600' },
              padding: 14,
              usePointStyle: true,
              pointStyle: 'circle'
            }
          },
          tooltip: {
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            titleFont: { family: 'Plus Jakarta Sans', size: 13, weight: '700' },
            bodyFont: { family: 'Plus Jakarta Sans', size: 12 },
            padding: 12,
            borderColor: 'rgba(255, 255, 255, 0.1)',
            borderWidth: 1,
            callbacks: {
              label: (item) => ` ${item.dataset.label}: ${item.raw.toFixed(2)} pts`
            }
          }
        },
        scales: {
          r: {
            angleLines: { color: 'rgba(255, 255, 255, 0.12)' },
            grid: { color: 'rgba(255, 255, 255, 0.08)' },
            pointLabels: {
              color: '#e5e7eb',
              font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' },
              padding: 8
            },
            ticks: {
              color: '#9ca3af',
              backdropColor: 'transparent',
              stepSize: 15,
              font: { size: 10 }
            },
            suggestedMin: 40,
            suggestedMax: 100
          }
        }
      }
    });
  }

  // Chart 4: Interannual Gaps Evolution (Bar Chart - EPEC vs Promedio >500k)
  const ctxGap500k = document.getElementById('chart-gap-500k');
  if (ctxGap500k) {
    new Chart(ctxGap500k.getContext('2d'), {
      type: 'bar',
      data: {
        labels: [
          'Suministro (SE)',
          'Facturación (FE)',
          'Atención (AT)',
          'Imagen (IM)',
          'Información (IC)',
          'Resp. Socioamb.',
          'ISCAL Global'
        ],
        datasets: [
          {
            label: 'EPEC 2025',
            data: [75.79, 70.21, 66.63, 56.54, 46.46, 55.34, 63.69],
            backgroundColor: 'rgba(139, 92, 246, 0.7)',
            borderColor: 'rgba(167, 139, 250, 1)',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'EPEC 2026',
            data: [78.48, 70.38, 68.10, 60.53, 52.03, 59.57, 65.96],
            backgroundColor: 'rgba(6, 182, 212, 0.85)',
            borderColor: 'rgba(34, 211, 238, 1)',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Prom. >500k 2025',
            data: [76.50, 71.80, 69.20, 62.10, 55.80, 58.60, 68.40],
            backgroundColor: 'rgba(107, 114, 128, 0.55)',
            borderColor: 'rgba(156, 163, 175, 1)',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Prom. >500k 2026',
            data: [77.80, 72.40, 70.50, 63.80, 57.40, 60.90, 70.15],
            backgroundColor: 'rgba(59, 130, 246, 0.8)',
            borderColor: 'rgba(96, 165, 250, 1)',
            borderWidth: 1,
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
            labels: {
              color: '#f3f4f6',
              font: { family: 'Plus Jakarta Sans', size: 11.5, weight: '600' },
              padding: 12,
              usePointStyle: true,
              pointStyle: 'rectRounded'
            }
          },
          tooltip: {
            backgroundColor: 'rgba(15, 23, 42, 0.95)',
            titleFont: { family: 'Plus Jakarta Sans', size: 13, weight: '700' },
            bodyFont: { family: 'Plus Jakarta Sans', size: 12 },
            padding: 12,
            borderColor: 'rgba(255, 255, 255, 0.1)',
            borderWidth: 1,
            callbacks: {
              label: (item) => ` ${item.dataset.label}: ${item.raw.toFixed(2)} pts`
            }
          }
        },
        scales: {
          x: {
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: {
              color: '#e5e7eb',
              font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' }
            }
          },
          y: {
            grid: { color: 'rgba(255, 255, 255, 0.08)' },
            ticks: {
              color: '#9ca3af',
              stepSize: 15,
              font: { size: 10 }
            },
            suggestedMin: 35,
            suggestedMax: 85
          }
        }
      }
    });
  }
}

// 3. Render Historical Comparative Table (2025 vs 2026)
let indicesData = (typeof DASHBOARD_DATA !== 'undefined') ? DASHBOARD_DATA.indices_comparativo : [];

function renderIndicesTable(filtered = null) {
  const tbody = document.getElementById('tbody-indices');
  if (!tbody) return;

  const list = filtered || indicesData;
  tbody.innerHTML = '';

  const countInfo = document.getElementById('table-count-info');
  if (countInfo) countInfo.textContent = `Mostrando ${list.length} indicadores`;

  list.forEach(item => {
    const tr = document.createElement('tr');
    
    const diffNum = parseFloat(item.Diferencia_Puntos);
    let diffClass = 'delta-neutral';
    let diffSign = '';
    if (!isNaN(diffNum)) {
      if (diffNum > 0) { diffClass = 'delta-up'; diffSign = '+'; }
      else if (diffNum < 0) { diffClass = 'delta-down'; }
    }

    const isHighlight = item.Sigla === 'ISCAL' || item.Sigla === 'IAC' || item.Tipo_Indice === 'IDAR';
    if (isHighlight) {
      tr.style.background = 'rgba(59, 130, 246, 0.06)';
      tr.style.fontWeight = '600';
    }

    tr.innerHTML = `
      <td><span style="color: var(--text-muted);">${item.Area_Dimension || '-'}</span></td>
      <td>${item.Sigla ? `<span class="sigla-tag">${item.Sigla}</span>` : '-'}</td>
      <td><span class="badge-tipo">${item.Tipo_Indice || '-'}</span></td>
      <td><strong style="color: white;">${item.Atributo_Indicador || item.Descripcion || '-'}</strong></td>
      <td style="color: #93c5fd;">${item.Indice_2025 !== undefined ? item.Indice_2025 : '-'}</td>
      <td style="color: #38bdf8;"><strong>${item.Indice_2026 !== undefined ? item.Indice_2026 : '-'}</strong></td>
      <td><span class="kpi-delta ${diffClass}">${diffSign}${item.Diferencia_Puntos}</span></td>
      <td><span class="kpi-delta ${diffClass}">${item.Variacion_IAOP_Pct}</span></td>
    `;
    tbody.appendChild(tr);
  });
}

// 4. Render Satisfaction Detail Table (2026)
function renderSatisfactionTable() {
  const tbody = document.getElementById('tbody-sat-detail');
  if (!tbody || typeof DASHBOARD_DATA === 'undefined') return;

  tbody.innerHTML = '';
  const list = DASHBOARD_DATA.indices_satisfaccion || [];

  list.forEach(item => {
    const tr = document.createElement('tr');
    const idx = parseFloat(item.Indice_Satisfaccion_100);
    
    let badgeHtml = '';
    if (idx >= 75) {
      badgeHtml = `<span class="badge badge-emerald">Excelente (${idx})</span>`;
    } else if (idx >= 65) {
      badgeHtml = `<span class="badge badge-cyan">Bueno (${idx})</span>`;
    } else if (idx >= 50) {
      badgeHtml = `<span class="badge badge-blue">Aceptable (${idx})</span>`;
    } else {
      badgeHtml = `<span class="badge badge-purple" style="background: rgba(244, 63, 94, 0.15); color: #fb7185; border-color: rgba(244, 63, 94, 0.3);">Oportunidad Mejora (${idx})</span>`;
    }

    tr.innerHTML = `
      <td><span style="color: var(--text-muted);">${item.Area_Dimension || '-'}</span></td>
      <td>${item.Sigla ? `<span class="sigla-tag">${item.Sigla}</span>` : '-'}</td>
      <td><strong>${item.Atributo_Evaluado || item.Atributo || '-'}</strong></td>
      <td style="color: #facc15; font-weight: 700;">★ ${item.Nota_Promedio_1_10 || '-'} / 10</td>
      <td><strong style="color: white;">${item.Indice_Satisfaccion_100 || '-'}</strong></td>
      <td>${badgeHtml}</td>
    `;
    tbody.appendChild(tr);
  });
}

// 5. Render Benchmark >500k Customers Table
let benchData = (typeof DASHBOARD_DATA !== 'undefined' && DASHBOARD_DATA.benchmark_500k) ? DASHBOARD_DATA.benchmark_500k : [];

function renderBenchmark500kTable(filtered = null) {
  const tbody = document.getElementById('tbody-benchmark-500k');
  if (!tbody) return;

  const list = filtered || benchData;
  tbody.innerHTML = '';

  const countInfo = document.getElementById('bench-count-info');
  if (countInfo) countInfo.textContent = `Mostrando ${list.length} indicadores benchmark`;

  list.forEach(item => {
    const tr = document.createElement('tr');

    const epec26 = parseFloat(item.epec_2026);
    const avg500k26 = parseFloat(item.avg_500k_2026);
    const isEpecAhead = !isNaN(epec26) && !isNaN(avg500k26) && (epec26 >= avg500k26);

    if (isEpecAhead && item.sigla !== 'IICP') {
      tr.style.background = 'rgba(16, 185, 129, 0.05)';
    }

    let statusBadge = '';
    if (item.estado.includes('Líder') || item.estado.includes('Fortaleza')) {
      statusBadge = `<span class="badge badge-emerald">🟢 ${item.estado}</span>`;
    } else if (item.estado.includes('Crecimiento') || item.estado.includes('Evolución') || item.estado.includes('Aceptable')) {
      statusBadge = `<span class="badge badge-cyan">🟡 ${item.estado}</span>`;
    } else if (item.estado.includes('Oportunidad')) {
      statusBadge = `<span class="badge badge-purple" style="background: rgba(244, 63, 94, 0.15); color: #fb7185; border-color: rgba(244, 63, 94, 0.3);">🔴 ${item.estado}</span>`;
    } else {
      statusBadge = `<span class="badge badge-blue">🔵 ${item.estado}</span>`;
    }

    const iaopStr = item.epec_iaop || '-';
    const isIaopPositive = iaopStr.startsWith('+');
    const iaopClass = isIaopPositive ? 'delta-up' : (iaopStr.startsWith('-') ? (item.sigla === 'IICP' ? 'delta-up' : 'delta-down') : 'delta-neutral');

    tr.innerHTML = `
      <td><strong style="color: white;">${item.area}</strong></td>
      <td>${item.sigla ? `<span class="sigla-tag">${item.sigla}</span>` : '-'}</td>
      <td><span class="badge-tipo">${item.tipo || '-'}</span></td>
      <td style="color: #93c5fd;">${item.epec_2025 !== undefined ? item.epec_2025 : '-'}</td>
      <td style="color: ${isEpecAhead ? '#34d399' : '#38bdf8'}; font-weight: 700;">${item.epec_2026 !== undefined ? item.epec_2026 : '-'}</td>
      <td><span class="kpi-delta ${iaopClass}">${iaopStr}</span></td>
      <td style="color: #9ca3af;">${item.avg_500k_2025 !== undefined ? item.avg_500k_2025 : '-'}</td>
      <td style="color: #e5e7eb; font-weight: 600;">${item.avg_500k_2026 !== undefined ? item.avg_500k_2026 : '-'}</td>
      <td style="color: #9ca3af;">${item.cier_total_2026 !== undefined ? item.cier_total_2026 : '-'}</td>
      <td style="color: #facc15; font-weight: 700;">★ ${item.benchmark_500k_2026 !== undefined ? item.benchmark_500k_2026 : '-'}</td>
      <td>
        <div>${statusBadge}</div>
        <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 0.25rem;">${item.posicion_relativa || ''}</div>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

// 6. Render Dictionary Table
let dictData = (typeof DASHBOARD_DATA !== 'undefined') ? DASHBOARD_DATA.diccionario : [];

function renderDictionaryTable(filtered = null) {
  const tbody = document.getElementById('tbody-dict');
  if (!tbody) return;

  const list = filtered || dictData;
  tbody.innerHTML = '';

  const countInfo = document.getElementById('dict-count-info');
  if (countInfo) countInfo.textContent = `Mostrando ${list.length} variables`;

  list.forEach(item => {
    const tr = document.createElement('tr');
    
    let statusBadge = '<span class="badge badge-blue">Presente en ambos</span>';
    if (item.Estado_Comparativo === 'Solo 2025') {
      statusBadge = '<span class="badge badge-purple">Solo 2025</span>';
    } else if (item.Estado_Comparativo && item.Estado_Comparativo.includes('Nueva')) {
      statusBadge = '<span class="badge badge-emerald">Nueva en 2026</span>';
    }

    const hasOptions = item.Opciones_2026 !== '{}' || item.Opciones_2025 !== '{}';
    const optBtn = hasOptions ? 
      `<button class="btn-action" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;" onclick="showOptionsModal('${item.Variable}')">Ver Opciones</button>` : 
      '<span style="color: var(--text-muted); font-size: 0.8rem;">Texto / Escala Libre</span>';

    tr.innerHTML = `
      <td><span class="sigla-tag" style="color: #67e8f9;">${item.Variable}</span></td>
      <td><span style="font-size: 0.82rem; color: var(--text-muted);">${formatDimensionName(item.Dimension_Tematica)}</span></td>
      <td><strong style="color: #e5e7eb;">${item.Descripcion_Consolidada || item.Descripcion_2026 || item.Descripcion_2025 || '-'}</strong></td>
      <td>${statusBadge}</td>
      <td>${optBtn}</td>
    `;
    tbody.appendChild(tr);
  });
}

function formatDimensionName(name) {
  if (!name) return '-';
  return name.replace(/^\d+_/, '').replace(/_/g, ' ');
}

// 6. Render File Explorer Grid
let filesData = (typeof DASHBOARD_DATA !== 'undefined') ? DASHBOARD_DATA.catalogo_archivos : [];

function renderFilesGrid(filtered = null) {
  const container = document.getElementById('files-grid-container');
  if (!container) return;

  const list = filtered || filesData;
  container.innerHTML = '';

  const countInfo = document.getElementById('file-count-info');
  if (countInfo) countInfo.textContent = `Mostrando ${list.length} archivos`;

  list.forEach(item => {
    const ext = (item.file_extension || '').replace('.', '').toLowerCase();
    let iconClass = 'icon-xlsx';
    let iconText = 'XLS';

    if (ext === 'pdf') { iconClass = 'icon-pdf'; iconText = 'PDF'; }
    else if (ext === 'pptx' || ext === 'ppt') { iconClass = 'icon-pptx'; iconText = 'PPT'; }
    else if (ext === 'csv') { iconClass = 'icon-csv'; iconText = 'CSV'; }
    else if (ext === 'json') { iconClass = 'icon-json'; iconText = 'JSON'; }

    const card = document.createElement('div');
    card.className = 'file-card';
    
    // Relative link to local extracted file
    const fileRelPath = `data/classified/${item.year}/${item.category}/${item.file_name}`;

    card.innerHTML = `
      <div class="file-card-top">
        <div class="file-icon ${iconClass}">${iconText}</div>
        <div class="file-info">
          <h4>${item.file_name}</h4>
          <div class="file-meta">
            <span class="badge ${item.year === 2026 ? 'badge-cyan' : 'badge-blue'}">${item.year}</span>
            <span>${item.size_kb} KB</span>
            <span>${item.modified_date || ''}</span>
          </div>
        </div>
      </div>
      <div style="font-size: 0.76rem; color: var(--text-muted); margin-bottom: 0.75rem;">
        📂 ${formatDimensionName(item.category)}
      </div>
      <div class="file-actions">
        <a href="${fileRelPath}" class="btn-action" target="_blank">📥 Abrir Archivo</a>
        <button class="btn-copy" onclick="copyPath('${fileRelPath}')">📋 Copiar</button>
      </div>
    `;
    container.appendChild(card);
  });
}

// 7. Filtering and Search Logic
function initFilters() {
  // Indices Search & Filter
  const searchIndices = document.getElementById('search-indices');
  const filterArea = document.getElementById('filter-area');
  const filterTipo = document.getElementById('filter-tipo');

  function applyIndicesFilter() {
    const q = (searchIndices ? searchIndices.value : '').toLowerCase();
    const area = filterArea ? filterArea.value : 'ALL';
    const tipo = filterTipo ? filterTipo.value : 'ALL';

    const filtered = indicesData.filter(item => {
      const matchQ = !q || 
        (item.Atributo_Indicador && item.Atributo_Indicador.toLowerCase().includes(q)) ||
        (item.Descripcion && item.Descripcion.toLowerCase().includes(q)) ||
        (item.Sigla && item.Sigla.toLowerCase().includes(q)) ||
        (item.Area_Dimension && item.Area_Dimension.toLowerCase().includes(q));

      const matchArea = area === 'ALL' || (item.Area_Dimension && item.Area_Dimension.includes(area));
      const matchTipo = tipo === 'ALL' || item.Tipo_Indice === tipo;

      return matchQ && matchArea && matchTipo;
    });

    renderIndicesTable(filtered);
  }

  if (searchIndices) searchIndices.addEventListener('input', applyIndicesFilter);
  if (filterArea) filterArea.addEventListener('change', applyIndicesFilter);
  if (filterTipo) filterTipo.addEventListener('change', applyIndicesFilter);

  // Dictionary Search & Filter
  const searchDict = document.getElementById('search-dict');
  const filterDictDim = document.getElementById('filter-dict-dim');
  const filterDictStatus = document.getElementById('filter-dict-status');

  function applyDictFilter() {
    const q = (searchDict ? searchDict.value : '').toLowerCase();
    const dim = filterDictDim ? filterDictDim.value : 'ALL';
    const status = filterDictStatus ? filterDictStatus.value : 'ALL';

    const filtered = dictData.filter(item => {
      const matchQ = !q || 
        (item.Variable && item.Variable.toLowerCase().includes(q)) ||
        (item.Descripcion_Consolidada && item.Descripcion_Consolidada.toLowerCase().includes(q));

      const matchDim = dim === 'ALL' || item.Dimension_Tematica === dim;
      const matchStatus = status === 'ALL' || item.Estado_Comparativo === status;

      return matchQ && matchDim && matchStatus;
    });

    renderDictionaryTable(filtered);
  }

  if (searchDict) searchDict.addEventListener('input', applyDictFilter);
  if (filterDictDim) filterDictDim.addEventListener('change', applyDictFilter);
  if (filterDictStatus) filterDictStatus.addEventListener('change', applyDictFilter);

  // Benchmark >500k Search & Filter
  const searchBench = document.getElementById('search-bench');
  const filterBenchTipo = document.getElementById('filter-bench-tipo');
  const filterBenchStatus = document.getElementById('filter-bench-status');

  function applyBenchFilter() {
    const q = (searchBench ? searchBench.value : '').toLowerCase();
    const tipo = filterBenchTipo ? filterBenchTipo.value : 'ALL';
    const status = filterBenchStatus ? filterBenchStatus.value : 'ALL';

    const filtered = benchData.filter(item => {
      const matchQ = !q || 
        (item.area && item.area.toLowerCase().includes(q)) ||
        (item.sigla && item.sigla.toLowerCase().includes(q)) ||
        (item.posicion_relativa && item.posicion_relativa.toLowerCase().includes(q));

      const matchTipo = tipo === 'ALL' || item.tipo === tipo;
      let matchStatus = true;
      if (status === 'Líder') {
        matchStatus = item.estado.includes('Líder') || item.estado.includes('Fortaleza');
      } else if (status === 'Crecimiento') {
        matchStatus = item.estado.includes('Crecimiento') || item.estado.includes('Evolución') || item.estado.includes('Aceptable');
      } else if (status === 'Oportunidad') {
        matchStatus = item.estado.includes('Oportunidad');
      }

      return matchQ && matchTipo && matchStatus;
    });

    renderBenchmark500kTable(filtered);
  }

  if (searchBench) searchBench.addEventListener('input', applyBenchFilter);
  if (filterBenchTipo) filterBenchTipo.addEventListener('change', applyBenchFilter);
  if (filterBenchStatus) filterBenchStatus.addEventListener('change', applyBenchFilter);

  // File Explorer Search & Filter
  const searchFiles = document.getElementById('search-files');
  const filterFileYear = document.getElementById('filter-file-year');
  const filterFileCat = document.getElementById('filter-file-cat');

  function applyFilesFilter() {
    const q = (searchFiles ? searchFiles.value : '').toLowerCase();
    const year = filterFileYear ? filterFileYear.value : 'ALL';
    const cat = filterFileCat ? filterFileCat.value : 'ALL';

    const filtered = filesData.filter(item => {
      const matchQ = !q || (item.file_name && item.file_name.toLowerCase().includes(q));
      const matchYear = year === 'ALL' || String(item.year) === year;
      const matchCat = cat === 'ALL' || item.category === cat;

      return matchQ && matchYear && matchCat;
    });

    renderFilesGrid(filtered);
  }

  if (searchFiles) searchFiles.addEventListener('input', applyFilesFilter);
  if (filterFileYear) filterFileYear.addEventListener('change', applyFilesFilter);
  if (filterFileCat) filterFileCat.addEventListener('change', applyFilesFilter);
}

// 8. Options Modal Display
function showOptionsModal(varName) {
  const item = dictData.find(d => d.Variable === varName);
  if (!item) return;

  const modal = document.getElementById('options-modal');
  const title = document.getElementById('modal-title');
  const body = document.getElementById('modal-body');

  title.textContent = `Variable: ${item.Variable} - ${item.Descripcion_Consolidada || ''}`;
  
  let opts26 = {};
  let opts25 = {};
  try { opts26 = JSON.parse(item.Opciones_2026 || '{}'); } catch(e){}
  try { opts25 = JSON.parse(item.Opciones_2025 || '{}'); } catch(e){}

  const activeOpts = Object.keys(opts26).length > 0 ? opts26 : opts25;

  let html = `
    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">
      Dimensión: <strong style="color: var(--accent-cyan);">${formatDimensionName(item.Dimension_Tematica)}</strong>
    </p>
    <div class="table-responsive">
      <table class="modern-table">
        <thead>
          <tr>
            <th style="width: 25%;">Código</th>
            <th>Significado / Etiqueta de Respuesta</th>
          </tr>
        </thead>
        <tbody>
  `;

  if (Object.keys(activeOpts).length === 0) {
    html += `<tr><td colspan="2" style="text-align: center; color: var(--text-muted);">Sin códigos fijos (Variable numérica o de escala abierta).</td></tr>`;
  } else {
    for (const [code, label] of Object.entries(activeOpts)) {
      html += `
        <tr>
          <td><span class="sigla-tag">${code}</span></td>
          <td><strong style="color: white;">${label}</strong></td>
        </tr>
      `;
    }
  }

  html += `</tbody></table></div>`;
  body.innerHTML = html;
  modal.classList.add('active');
}

function closeModal() {
  const modal = document.getElementById('options-modal');
  if (modal) modal.classList.remove('active');
}

// 9. Copy Path to Clipboard Helper
function copyPath(relPath) {
  const fullPath = `C:\\Users\\jidiaz\\.gemini\\antigravity-ide\\scratch\\encuesta_cier\\${relPath.replace(/\//g, '\\')}`;
  navigator.clipboard.writeText(fullPath).then(() => {
    showToast(`Ruta copiada: ${fullPath.split('\\').pop()}`);
  }).catch(() => {
    showToast(`Ruta: ${fullPath}`);
  });
}

function showToast(msg) {
  const toast = document.getElementById('toast-notice');
  if (!toast) return;
  toast.textContent = msg;
  toast.style.display = 'block';
  setTimeout(() => {
    toast.style.display = 'none';
  }, 2500);
}
