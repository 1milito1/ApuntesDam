/**
 * APUNTES DAM - APLICACIÓN PRINCIPAL
 * Diseñado para GitHub Pages y navegación de alto rendimiento con +790 documentos
 */

(function () {
  'use strict';

  // State
  let appData = {
    cursos: [],
    categorias: [],
    documentos: []
  };

  let filterState = {
    curso: 'all',
    asignatura: 'all',
    categoria: 'all',
    formato: 'all',
    search: '',
    tag: null,
    sortBy: 'az'
  };

  const ITEMS_PER_PAGE = 36;
  let currentRenderLimit = ITEMS_PER_PAGE;

  // DOM Elements
  const el = {
    themeToggle: document.getElementById('theme-toggle'),
    searchInput: document.getElementById('search-input'),
    clearSearchBtn: document.getElementById('clear-search-btn'),
    courseTabs: document.getElementById('course-tabs'),
    subjectSelect: document.getElementById('subject-select'),
    formatSelect: document.getElementById('format-select'),
    categoryPills: document.getElementById('category-pills'),
    sortSelect: document.getElementById('sort-select'),
    cardsGrid: document.getElementById('cards-grid'),
    resultsCount: document.getElementById('results-count'),
    loadMoreContainer: document.getElementById('load-more-container'),
    loadMoreBtn: document.getElementById('btn-load-more'),
    statDocs: document.getElementById('stat-docs'),
    statAsignaturas: document.getElementById('stat-asignaturas'),
    statExamenes: document.getElementById('stat-examenes'),
    statTareas: document.getElementById('stat-tareas'),
    modalBackdrop: document.getElementById('modal-backdrop'),
    modalCloseBtn: document.getElementById('modal-close-btn'),
    modalTitle: document.getElementById('modal-title'),
    modalSub: document.getElementById('modal-sub'),
    modalBody: document.getElementById('modal-body'),
    modalDownloadBtn: document.getElementById('modal-download-btn'),
    modalCopyBtn: document.getElementById('modal-copy-btn'),
    btnOpenContact: document.getElementById('btn-open-contact'),
    contactModalBackdrop: document.getElementById('contact-modal-backdrop'),
    contactModalCloseBtn: document.getElementById('contact-modal-close-btn'),
    btnCancelContact: document.getElementById('btn-cancel-contact'),
    contactForm: document.getElementById('contact-form'),
    contactSender: document.getElementById('contact-sender'),
    contactTitle: document.getElementById('contact-title'),
    contactMessage: document.getElementById('contact-message'),
    btnSubmitContact: document.getElementById('btn-submit-contact'),
    contactStatus: document.getElementById('contact-status'),
    toast: document.getElementById('toast'),
    toastMsg: document.getElementById('toast-msg')
  };

  // Initial Load
  init();

  async function init() {
    initTheme();
    setupEventListeners();
    await loadData();
    populateSubjectFilter();
    updateStats();
    renderCards();
  }

  // Load Data: Try window.INITIAL_DATA first, then fetch fallback
  async function loadData() {
    if (window.INITIAL_DATA && window.INITIAL_DATA.documentos) {
      appData = window.INITIAL_DATA;
      return;
    }

    try {
      const res = await fetch('data/apuntes.json');
      if (res.ok) {
        appData = await res.json();
      }
    } catch (err) {
      console.warn('CORS or fetch error loading data/apuntes.json, using fallback', err);
    }
  }

  // Theme Management
  function initTheme() {
    const savedTheme = localStorage.getItem('dam_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (el.themeToggle) {
      el.themeToggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('dam_theme', next);
        updateThemeIcon(next);
      });
    }
  }

  function updateThemeIcon(theme) {
    if (!el.themeToggle) return;
    el.themeToggle.innerHTML = theme === 'dark' 
      ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
      : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }

  // Event Listeners
  function setupEventListeners() {
    // Search input with debounce
    let debounceTimer;
    if (el.searchInput) {
      el.searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          filterState.search = e.target.value.trim().toLowerCase();
          currentRenderLimit = ITEMS_PER_PAGE;
          if (el.clearSearchBtn) {
            el.clearSearchBtn.style.display = filterState.search ? 'block' : 'none';
          }
          renderCards();
        }, 120);
      });
    }

    if (el.clearSearchBtn) {
      el.clearSearchBtn.addEventListener('click', () => {
        el.searchInput.value = '';
        filterState.search = '';
        currentRenderLimit = ITEMS_PER_PAGE;
        el.clearSearchBtn.style.display = 'none';
        renderCards();
      });
    }

    // Keyboard shortcut (Ctrl+K or /)
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey && e.key.toLowerCase() === 'k') || (e.key === '/' && document.activeElement !== el.searchInput)) {
        e.preventDefault();
        el.searchInput.focus();
        el.searchInput.select();
      }
      if (e.key === 'Escape') {
        if (el.modalBackdrop && el.modalBackdrop.classList.contains('open')) closeModal();
        if (el.contactModalBackdrop && el.contactModalBackdrop.classList.contains('open')) closeContactModal();
      }
    });

    // Course Tabs
    if (el.courseTabs) {
      el.courseTabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.tab-btn');
        if (!btn) return;
        el.courseTabs.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterState.curso = btn.dataset.curso;
        filterState.asignatura = 'all';
        currentRenderLimit = ITEMS_PER_PAGE;
        populateSubjectFilter();
        renderCards();
      });
    }

    // Dropdowns
    if (el.subjectSelect) {
      el.subjectSelect.addEventListener('change', (e) => {
        filterState.asignatura = e.target.value;
        currentRenderLimit = ITEMS_PER_PAGE;
        renderCards();
      });
    }

    if (el.formatSelect) {
      el.formatSelect.addEventListener('change', (e) => {
        filterState.formato = e.target.value;
        currentRenderLimit = ITEMS_PER_PAGE;
        renderCards();
      });
    }

    if (el.sortSelect) {
      el.sortSelect.addEventListener('change', (e) => {
        filterState.sortBy = e.target.value;
        currentRenderLimit = ITEMS_PER_PAGE;
        renderCards();
      });
    }

    // Category pills
    if (el.categoryPills) {
      el.categoryPills.addEventListener('click', (e) => {
        const pill = e.target.closest('.cat-pill');
        if (!pill) return;
        el.categoryPills.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        filterState.categoria = pill.dataset.cat;
        currentRenderLimit = ITEMS_PER_PAGE;
        renderCards();
      });
    }

    // Load more button
    if (el.loadMoreBtn) {
      el.loadMoreBtn.addEventListener('click', () => {
        currentRenderLimit += ITEMS_PER_PAGE;
        renderCards(true);
      });
    }

    // Modal close
    if (el.modalCloseBtn) {
      el.modalCloseBtn.addEventListener('click', closeModal);
    }
    if (el.modalBackdrop) {
      el.modalBackdrop.addEventListener('click', (e) => {
        if (e.target === el.modalBackdrop) closeModal();
      });
    }

    // Contact Modal listeners
    if (el.btnOpenContact) {
      el.btnOpenContact.addEventListener('click', openContactModal);
    }
    if (el.contactModalCloseBtn) {
      el.contactModalCloseBtn.addEventListener('click', closeContactModal);
    }
    if (el.btnCancelContact) {
      el.btnCancelContact.addEventListener('click', closeContactModal);
    }
    if (el.contactModalBackdrop) {
      el.contactModalBackdrop.addEventListener('click', (e) => {
        if (e.target === el.contactModalBackdrop) closeContactModal();
      });
    }

    // Contact Form Submit via Hidden Iframe (No mail app, no CORS freezing)
    const hiddenIframe = document.getElementById('contact_hidden_iframe');
    const hiddenSubject = document.getElementById('contact-hidden-subject');

    if (el.contactForm) {
      el.contactForm.addEventListener('submit', (e) => {
        const sender = el.contactSender ? el.contactSender.value.trim() : '';
        const title = el.contactTitle ? el.contactTitle.value.trim() : '';
        const message = el.contactMessage ? el.contactMessage.value.trim() : '';

        if (!sender || !title || !message) {
          e.preventDefault();
          return;
        }

        if (hiddenSubject) {
          hiddenSubject.value = `[Apuntes DAM] ${title} (De: ${sender})`;
        }

        if (el.btnSubmitContact) {
          el.btnSubmitContact.disabled = true;
          el.btnSubmitContact.textContent = 'Enviando...';
        }
        if (el.contactStatus) {
          el.contactStatus.style.display = 'block';
          el.contactStatus.style.background = 'var(--primary-light)';
          el.contactStatus.style.color = 'var(--primary)';
          el.contactStatus.textContent = 'Enviando mensaje...';
        }

        // The form submits naturally to the hidden iframe
        // Show success confirmation after submission is processed
        let handled = false;
        const markSuccess = () => {
          if (handled) return;
          handled = true;
          if (el.contactStatus) {
            el.contactStatus.style.background = 'rgba(16, 185, 129, 0.15)';
            el.contactStatus.style.color = 'var(--success)';
            el.contactStatus.textContent = '✓ ¡Mensaje enviado con éxito! Gracias por tu aportación.';
          }
          showToast('Mensaje enviado con éxito');
          setTimeout(() => {
            closeContactModal();
            if (el.contactForm) el.contactForm.reset();
            if (el.contactStatus) el.contactStatus.style.display = 'none';
            if (el.btnSubmitContact) {
              el.btnSubmitContact.disabled = false;
              el.btnSubmitContact.textContent = 'Enviar Mensaje';
            }
          }, 2000);
        };

        if (hiddenIframe) {
          hiddenIframe.onload = markSuccess;
        }
        // Fallback timer ensures it NEVER stays stuck
        setTimeout(markSuccess, 1800);
      });
    }
  }

  function openContactModal() {
    if (!el.contactModalBackdrop) return;
    el.contactModalBackdrop.classList.add('open');
    if (el.contactStatus) el.contactStatus.style.display = 'none';
    if (el.btnSubmitContact) {
      el.btnSubmitContact.disabled = false;
      el.btnSubmitContact.textContent = 'Enviar Mensaje';
    }
    if (el.contactSender) el.contactSender.focus();
  }

  function closeContactModal() {
    if (!el.contactModalBackdrop) return;
    el.contactModalBackdrop.classList.remove('open');
  }

  // Populate dynamic subjects dropdown
  function populateSubjectFilter() {
    if (!el.subjectSelect) return;
    el.subjectSelect.innerHTML = '<option value="all">Todas las asignaturas</option>';

    let available = [];
    if (filterState.curso === 'all') {
      appData.cursos.forEach(c => {
        available.push(...c.asignaturas.map(a => ({ ...a, cursoId: c.id, cursoName: c.name })));
      });
    } else {
      const found = appData.cursos.find(c => c.id === filterState.curso);
      if (found) {
        available = found.asignaturas.map(a => ({ ...a, cursoId: found.id, cursoName: found.name }));
      }
    }

    available.forEach(a => {
      const opt = document.createElement('option');
      opt.value = a.id;
      opt.textContent = `${a.name} (${a.code})`;
      if (filterState.asignatura === a.id) opt.selected = true;
      el.subjectSelect.appendChild(opt);
    });
  }

  // Update Stats Counter
  function updateStats() {
    const docs = appData.documentos || [];
    if (el.statDocs) el.statDocs.textContent = docs.length;

    // Unique subjects with content
    const subjects = new Set(docs.map(d => d.asignatura));
    if (el.statAsignaturas) el.statAsignaturas.textContent = subjects.size;

    const examenes = docs.filter(d => d.categoria === 'examenes').length;
    if (el.statExamenes) el.statExamenes.textContent = examenes;

    const tareas = docs.filter(d => d.categoria === 'tareas').length;
    if (el.statTareas) el.statTareas.textContent = tareas;
  }

  // Filter & Sort Logic
  function getFilteredDocuments() {
    return (appData.documentos || []).filter(doc => {
      // Course
      if (filterState.curso !== 'all' && doc.curso !== filterState.curso) return false;
      // Subject
      if (filterState.asignatura !== 'all' && doc.asignatura !== filterState.asignatura) return false;
      // Category
      if (filterState.categoria !== 'all' && doc.categoria !== filterState.categoria) return false;
      // Format
      if (filterState.formato !== 'all') {
        if (filterState.formato === 'pdf' && doc.fileType !== 'pdf') return false;
        if (filterState.formato === 'docx' && !['docx', 'doc'].includes(doc.fileType)) return false;
        if (filterState.formato === 'code' && !['md', 'sql', 'java', 'py', 'txt', 'html', 'css'].includes(doc.fileType)) return false;
        if (filterState.formato === 'zip' && !['zip', 'rar'].includes(doc.fileType)) return false;
      }
      // Tag
      if (filterState.tag && !doc.tags.includes(filterState.tag)) return false;

      // Text Search
      if (filterState.search) {
        const query = filterState.search;
        const inTitle = doc.title.toLowerCase().includes(query);
        const inDesc = (doc.description || '').toLowerCase().includes(query);
        const inAsig = (doc.asignaturaName || '').toLowerCase().includes(query);
        const inTags = (doc.tags || []).some(t => t.toLowerCase().includes(query));
        const inExt = doc.fileType.toLowerCase().includes(query);
        const inFilename = doc.filename.toLowerCase().includes(query);
        if (!inTitle && !inDesc && !inAsig && !inTags && !inExt && !inFilename) return false;
      }

      return true;
    }).sort((a, b) => {
      if (filterState.sortBy === 'az') return a.title.localeCompare(b.title);
      if (filterState.sortBy === 'subject') return a.asignaturaName.localeCompare(b.asignaturaName);
      // 'recent'
      return (b.date || '').localeCompare(a.date || '');
    });
  }

  // Render Cards Grid
  function renderCards(keepScroll) {
    const list = getFilteredDocuments();
    const visibleList = list.slice(0, currentRenderLimit);

    if (el.resultsCount) {
      el.resultsCount.innerHTML = `Mostrando <strong>${Math.min(visibleList.length, list.length)}</strong> de <strong>${list.length}</strong> documentos${filterState.tag ? ` con etiqueta "<strong>${filterState.tag}</strong>" <button id="btn-clear-tag" style="background:none;border:none;color:var(--primary);cursor:pointer;margin-left:6px;font-weight:600;">(quitar filtro)</button>` : ''}`;
      const clearTagBtn = document.getElementById('btn-clear-tag');
      if (clearTagBtn) {
        clearTagBtn.addEventListener('click', () => {
          filterState.tag = null;
          renderCards();
        });
      }
    }

    if (el.loadMoreContainer) {
      el.loadMoreContainer.style.display = list.length > currentRenderLimit ? 'block' : 'none';
      if (el.loadMoreBtn) {
        el.loadMoreBtn.textContent = `Cargar más documentos (${list.length - visibleList.length} restantes) ↓`;
      }
    }

    if (list.length === 0) {
      el.cardsGrid.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">📂</div>
          <h3>No se han encontrado apuntes</h3>
          <p>Prueba con otros términos de búsqueda o cambia los filtros de curso o asignatura.</p>
          <button class="btn-pill btn-primary" id="btn-reset-filters">Restablecer todos los filtros</button>
        </div>
      `;
      const resetBtn = document.getElementById('btn-reset-filters');
      if (resetBtn) {
        resetBtn.addEventListener('click', resetFilters);
      }
      return;
    }

    el.cardsGrid.innerHTML = visibleList.map(doc => {
      // Find subject color
      let asigColor = '#6366f1';
      for (const c of appData.cursos) {
        const found = c.asignaturas.find(a => a.id === doc.asignatura);
        if (found && found.color) {
          asigColor = found.color;
          break;
        }
      }

      const tagsHtml = (doc.tags || []).map(t => `<span class="tag-item" data-tag="${escapeHtml(t)}">#${escapeHtml(t)}</span>`).join('');

      return `
        <article class="doc-card" style="--card-accent: ${asigColor};">
          <div>
            <div class="card-badges">
              <span class="badge badge-curso">${escapeHtml(doc.cursoName)}</span>
              <span class="badge badge-asig" style="--asig-color: ${asigColor}; --asig-bg: ${hexToRgba(asigColor, 0.15)};">${escapeHtml(doc.asignaturaName)}</span>
              <span class="badge badge-${escapeHtml(doc.categoria)}">${escapeHtml(doc.categoriaName)}</span>
            </div>

            <h2 class="doc-title" data-doc-id="${doc.id}">${escapeHtml(doc.title)}</h2>
            <p class="doc-description">${escapeHtml(doc.description || '')}</p>

            <div class="tags-list">
              ${tagsHtml}
            </div>
          </div>

          <div class="card-footer">
            <div class="file-meta">
              <span class="file-format">${doc.fileType}</span>
              <span>${doc.fileSize || ''}</span>
            </div>

            <div class="card-actions">
              <button class="btn-card-action btn-card-primary btn-preview" data-doc-id="${doc.id}">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                Ver
              </button>
              <a href="${doc.relPath}" download class="btn-card-action" title="Descargar archivo">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </a>
              <button class="btn-card-action btn-copy-link" data-path="${doc.relPath}" title="Copiar enlace">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
              </button>
            </div>
          </div>
        </article>
      `;
    }).join('');

    // Attach card event listeners
    el.cardsGrid.querySelectorAll('.doc-title, .btn-preview').forEach(b => {
      b.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.docId;
        openDocumentModal(id);
      });
    });

    el.cardsGrid.querySelectorAll('.tag-item').forEach(tagEl => {
      tagEl.addEventListener('click', (e) => {
        filterState.tag = e.currentTarget.dataset.tag;
        currentRenderLimit = ITEMS_PER_PAGE;
        renderCards();
      });
    });

    el.cardsGrid.querySelectorAll('.btn-copy-link').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const path = e.currentTarget.dataset.path;
        const fullUrl = new URL(path, window.location.href).href;
        navigator.clipboard.writeText(fullUrl).then(() => {
          showToast('Enlace copiado al portapapeles');
        });
      });
    });
  }

  function resetFilters() {
    filterState = {
      curso: 'all',
      asignatura: 'all',
      categoria: 'all',
      formato: 'all',
      search: '',
      tag: null,
      sortBy: 'az'
    };
    currentRenderLimit = ITEMS_PER_PAGE;
    if (el.searchInput) el.searchInput.value = '';
    if (el.clearSearchBtn) el.clearSearchBtn.style.display = 'none';
    if (el.courseTabs) {
      el.courseTabs.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.toggle('active', b.dataset.curso === 'all');
      });
    }
    if (el.categoryPills) {
      el.categoryPills.querySelectorAll('.cat-pill').forEach(p => {
        p.classList.toggle('active', p.dataset.cat === 'all');
      });
    }
    if (el.subjectSelect) el.subjectSelect.value = 'all';
    if (el.formatSelect) el.formatSelect.value = 'all';
    if (el.sortSelect) el.sortSelect.value = 'az';
    populateSubjectFilter();
    renderCards();
  }

  // Modal Open & Render Content
  async function openDocumentModal(id) {
    const doc = (appData.documentos || []).find(d => d.id === id);
    if (!doc) return;

    el.modalTitle.textContent = doc.title;
    el.modalSub.textContent = `${doc.cursoName} • ${doc.asignaturaName} • ${doc.categoriaName} • ${doc.filename}`;
    el.modalDownloadBtn.href = doc.relPath;
    el.modalDownloadBtn.setAttribute('download', doc.filename);

    el.modalBody.innerHTML = `
      <div style="text-align: center; padding: 3rem; color: var(--text-muted);">
        <p>Cargando previsualización...</p>
      </div>
    `;
    el.modalBackdrop.classList.add('open');

    // Handle Copy Content Button
    let currentRawContent = '';
    el.modalCopyBtn.onclick = () => {
      if (currentRawContent) {
        navigator.clipboard.writeText(currentRawContent).then(() => {
          showToast('Contenido copiado al portapapeles');
        });
      }
    };

    try {
      if (doc.fileType === 'pdf') {
        el.modalBody.innerHTML = `
          <div style="height: 65vh; width: 100%;">
            <iframe src="${doc.relPath}" width="100%" height="100%" style="border: none; border-radius: 8px;"></iframe>
          </div>
        `;
        currentRawContent = new URL(doc.relPath, window.location.href).href;
        return;
      }

      if (['zip', 'rar', 'docx', 'doc', 'pptx'].includes(doc.fileType)) {
        el.modalBody.innerHTML = `
          <div style="padding: 2.5rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📦</div>
            <h3 style="margin-bottom: 0.5rem;">${escapeHtml(doc.filename)}</h3>
            <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
              Archivo <strong>${doc.fileType.toUpperCase()}</strong> (${doc.fileSize}). Puedes descargarlo directamente para abrirlo en tu equipo con Office o descompresor.
            </p>
            <a href="${doc.relPath}" download class="btn-pill btn-primary" style="padding: 0.75rem 1.75rem;">
              Descargar ${escapeHtml(doc.filename)}
            </a>
          </div>
        `;
        currentRawContent = new URL(doc.relPath, window.location.href).href;
        return;
      }

      // Fetch text or code
      const res = await fetch(doc.relPath);
      if (!res.ok) throw new Error('No se pudo cargar el archivo');
      const text = await res.text();
      currentRawContent = text;

      if (['md', 'markdown'].includes(doc.fileType)) {
        el.modalBody.innerHTML = parseSimpleMarkdown(text);
      } else {
        el.modalBody.innerHTML = `
          <pre><code class="language-${doc.fileType}">${escapeHtml(text)}</code></pre>
        `;
      }
    } catch (err) {
      el.modalBody.innerHTML = `
        <div style="padding: 2rem; text-align: center;">
          <p style="color: var(--danger); font-weight: 600; margin-bottom: 0.5rem;">Previsualización directa no disponible</p>
          <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Puedes descargar el archivo directamente para abrirlo en tu equipo.</p>
          <a href="${doc.relPath}" download class="btn-pill btn-primary">Descargar ${escapeHtml(doc.filename)}</a>
        </div>
      `;
    }
  }

  function closeModal() {
    el.modalBackdrop.classList.remove('open');
  }

  // Toast Notification
  function showToast(msg) {
    if (!el.toast) return;
    el.toastMsg.textContent = msg;
    el.toast.classList.add('show');
    setTimeout(() => {
      el.toast.classList.remove('show');
    }, 3000);
  }

  // Simple Markdown Parser
  function parseSimpleMarkdown(md) {
    let html = escapeHtml(md);

    // Code blocks with syntax formatting
    html = html.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, function (_, lang, code) {
      return `<pre><code class="language-${lang}">${code}</code></pre>`;
    });

    // Inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Headers
    html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');

    // Horizontal rule
    html = html.replace(/^---$/gim, '<hr style="border:none;border-top:1px solid var(--border-color);margin:1.5rem 0;" />');

    // Bold & Italic
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');

    // Tables
    html = html.replace(/\|(.+)\|/g, function (match) {
      const cells = match.split('|').filter((_, i, arr) => i > 0 && i < arr.length - 1);
      if (match.includes('---')) {
        return '';
      }
      const tdType = match.includes('---') ? 'th' : 'td';
      const row = cells.map(c => `<${tdType}>${c.trim()}</${tdType}>`).join('');
      return `<tr>${row}</tr>`;
    });
    html = html.replace(/(<tr>[\s\S]*?<\/tr>)+/g, '<div style="overflow-x:auto;"><table>$&</table></div>');

    // Lists
    html = html.replace(/^\s*[-*]\s+(.*$)/gim, '<li>$1</li>');
    html = html.replace(/(<li>[\s\S]*?<\/li>)+/g, '<ul>$&</ul>');

    // Paragraphs
    html = html.replace(/\n\n+/g, '</p><p>');
    html = '<p>' + html + '</p>';
    html = html.replace(/<p>\s*<\/p>/g, '');
    html = html.replace(/<p>\s*(<h[1-3]>[\s\S]*?<\/h[1-3]>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<pre>[\s\S]*?<\/pre>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<div[\s\S]*?<\/div>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<ul>[\s\S]*?<\/ul>)\s*<\/p>/g, '$1');
    html = html.replace(/<p>\s*(<hr.*?>)\s*<\/p>/g, '$1');

    return html;
  }

  // Utility helpers
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function hexToRgba(hex, alpha) {
    hex = hex.replace('#', '');
    if (hex.length === 3) {
      hex = hex.split('').map(c => c + c).join('');
    }
    const r = parseInt(hex.substring(0, 2), 16) || 99;
    const g = parseInt(hex.substring(2, 4), 16) || 102;
    const b = parseInt(hex.substring(4, 6), 16) || 241;
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
  }

})();
