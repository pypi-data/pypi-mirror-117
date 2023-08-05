/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 158);
/******/ })
/************************************************************************/
/******/ ({

/***/ 10:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRCookiebar {
  constructor(name, component, data, lang, callback) {
    this.name = name
    this.component = component
    this.data = this._setData(data, lang)
    this.callback = callback
    this._setUp()
    this._setBehavior()
  }

  _setData(data, lang) {
    if (data) {
      const dataObj = JSON.parse(data).filter((obj) => {
        return obj.lang === lang
      })
      if (dataObj.length > 0) {
        return dataObj[0]
      } else {
        return JSON.parse(data)[0]
      }
    } else {
      return null
    }
  }

  _setUp() {
    this._setAllOptOut()
    this._setGroupOptOut()
    this._setCookieOptOut()
    this._setPriorityValues()
    this._setConsistency()
    this._setPrimaryButton()
    this._setSecondaryButton()
    this._setCloseButton()
    this._setInfoText()
    this._setMainTitle()
    this._setLastUpdate()
    this._setListHeader()
    this._setEntryText()
    this._setGroupInfo()
    this._setNotification()
    this._setLinks()
  }

  _setBehavior() {
    this._setGroupBehavior()
    this._setCookieSelection()
    this._setAcceptBehavior()
    this._setOutputJSON()
    this._setResize()
  }

  _setPrimaryButton() {
    this.component
      .querySelectorAll('.actions .br-button.primary')
      .forEach((button) => {
        if (this.data.acceptButton && this.data.acceptButton.length > 0) {
          button.innerHTML = this.data.acceptButton
        } else {
          button.innerHTML = 'Aceitar'
        }
        if (window.matchMedia('(max-width: 574px)').matches) {
          button.classList.add('block')
        }
        if (window.matchMedia('(min-width: 575px)').matches) {
          button.classList.remove('block')
        }
      })
  }

  _setSecondaryButton() {
    this.component
      .querySelectorAll('.actions .br-button.secondary')
      .forEach((button) => {
        if (this.data.allOptOut) {
          if (this.data.optOutButton && this.data.optOutButton.length > 0) {
            button.innerHTML = this.data.optOutButton
          } else {
            button.innerHTML = 'Definir Cookies'
          }
        } else {
          if (this.data.optInButton && this.data.optInButton.length > 0) {
            button.innerHTML = this.data.optInButton
          } else {
            button.innerHTML = 'Ver Política de Cookies'
          }
        }

        if (window.matchMedia('(max-width: 574px)').matches) {
          button.classList.add('block')
        }
        if (window.matchMedia('(min-width: 575px)').matches) {
          button.classList.remove('block')
        }

        // Expande o cookiebar
        button.addEventListener('click', () => {
          this.component.classList.remove('default')
          button.classList.add('d-none')
          document.body.style.overflowY = 'hidden'
          this._setOpenView()
        })
      })
  }

  _setCloseButton() {
    this.component
      .querySelectorAll('.br-modal-header .close')
      .forEach((closeButton) => {
        // encolhe o cookiebar (volta ao cookiebar default)
        closeButton.addEventListener('click', () => {
          // this.component.classList.remove('active')
          this.component.classList.add('default')
          this.component
            .querySelector('.actions .br-button.secondary')
            .classList.remove('d-none')
          document.body.style.overflowY = 'auto'
          this._setCloseView()
        })
      })
  }

  _setOpenView() {
    const wrapper = this.component.querySelector(
      '.br-modal > .br-card .wrapper'
    )
    const containerFluid = this.component.querySelector(
      '.br-modal > .br-card .container-fluid'
    )
    const padding = window
      .getComputedStyle(containerFluid, null)
      .getPropertyValue('padding')
      .match(/\d+/)
    const height = `${window.innerHeight - padding * 2}px`
    wrapper.style.height = height
  }

  _setCloseView() {
    const wrapper = this.component.querySelector(
      '.br-modal > .br-card .wrapper'
    )
    wrapper.removeAttribute('style')
  }

  _setResize() {
    window.addEventListener('resize', () => {
      if (!this.component.classList.contains('default')) {
        this._setOpenView()
      }
      this.component
        .querySelectorAll('.actions .br-button')
        .forEach((button) => {
          if (window.matchMedia('(max-width: 574px)').matches) {
            button.classList.add('block')
          }
          if (window.matchMedia('(min-width: 575px)').matches) {
            button.classList.remove('block')
          }
        })
    })
  }

  _setInfoText() {
    this.component
      .querySelectorAll('.br-modal-body .info-text')
      .forEach((infoText) => {
        infoText.innerHTML = this.data.infoText
      })
  }

  _setMainTitle() {
    this.component
      .querySelectorAll('.br-modal-header .br-modal-title')
      .forEach((mainTitle) => {
        const title = `<div class="row">
                        <div class="col">
                          <p>${this.data.mainTitle}</p>
                        </div>
                      </div>`
        mainTitle.innerHTML = title
      })
  }

  _setLastUpdate() {
    if (this.data.lastUpdate) {
      this.component
        .querySelectorAll('.br-modal-header .last-update')
        .forEach((lastUpdate) => {
          lastUpdate.innerHTML = `Última atualização: <span>${this.data.lastUpdate}</span>`
        })
    }
  }

  _setListHeader() {
    this.component
      .querySelectorAll('.br-modal-body .main-content')
      .forEach((mainContent) => {
        const listHeader = `<div class="header">
                            <div class="row justify-content-between flex-fill">
                              <div class="col align-self-center">
                                <div class="title">Classes de cookies</div>
                              </div>
                              <div class="col-auto">
                                ${
                                  this.data.allOptOut
                                    ? this._createSwitchAll(this.data.selectAll)
                                    : ''
                                }
                              </div>
                            </div>
                          </div>`
        mainContent.insertAdjacentHTML('afterbegin', listHeader)
      })
  }

  _setEntryText() {
    this.component
      .querySelectorAll('.br-modal-header .entry-text')
      .forEach((entryText) => {
        entryText.innerHTML = this.data.entryText
      })
  }

  _setGroupInfo() {
    this.component
      .querySelectorAll('.br-modal-body .main-content')
      .forEach((mainContent) => {
        this.data.cookieGroups.forEach((item, index) => {
          const group = `<hr>
                      <div class="br-item group-info">
                        <div class="row mb-1">
                          <div class="col align-self-center">
                            <span class="group-name">${item.groupName}</span>
                            <span class="group-size">(${
                              item.cookieList.length
                            })</span>
                          </div>
                          <div class="col-2-auto align-self-center d-flex justify-content-lg-end">
                            ${
                              item.groupOptOut
                                ? this._createSwitchButton(
                                    index,
                                    'group-',
                                    item.groupSelected
                                  )
                                : '<span class="always-active">Sempre ativo</span>'
                            }
                          </div>
                          <div class="col-auto align-self-center">
                            <button class="br-button circle small" type="button"><i class="fas fa-angle-down" aria-hidden="true"></i>
                            </button>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col">
                            <p class="group-description">${item.groupText}</p>
                          </div>
                        </div>
                      </div>
                      <div class="br-list cookie-info">
                        <div class="br-item">
                          <div class="row">
                            <div class="col">
                              ${this._buildCookieInfo(index, item.cookieList)}
                            </div>
                          </div>
                        </div>
                      </div>`

          mainContent.insertAdjacentHTML('beforeend', group)
        })
      })
  }

  _setNotification() {
    if (this.data.noteList && this.data.noteList.length > 0) {
      this.component
        .querySelectorAll('.br-modal-body .main-content')
        .forEach((mainContent) => {
          const note = `<hr>
                      <div class="br-item">
                      <div class="row">
                        <div class="col align-self-center">
                          <span class="group-name">${this.data.noteTitle}</span>
                        </div>
                        <div class="col-auto">
                          <button class="br-button circle small" type="button"><i class="fas fa-angle-down" aria-hidden="true"></i>
                          </button>
                        </div>
                      </div>
                    </div>
                    <div class="br-list">
                      ${this._buildNotificationInfo()}
                    </div>`

          mainContent.insertAdjacentHTML('beforeend', note)
        })
    }
  }

  _setLinks() {
    if (this.data.links && this.data.links.length > 0) {
      this.component.querySelectorAll('.br-modal-body').forEach((modalBody) => {
        const link = `<div class="br-list parallel-content">
                        ${this._buildLinkInfo()}
                      </div>`

        modalBody.insertAdjacentHTML('beforeend', link)
      })
    }
  }

  _buildCookieInfo(groupIndex, cookieList) {
    let cookieInfo = ''
    cookieList.forEach((cookie, index) => {
      cookieInfo += `<div class="br-card">
                      <div class="card-content">
                        <div class="row mb-1">
                          <div class="col text-right">
                            ${
                              cookie.cookieOptOut
                                ? this._createSwitchButton(
                                    index,
                                    `cookie-${groupIndex}`,
                                    cookie.cookieSelected
                                  )
                                : ''
                            }
                          </div>
                        </div>
                        <div class="row mb-1">
                          ${
                            !cookie.cookieSelected && cookie.alertMessage
                              ? `<div class="col text-right message">
                                  <span class="feedback warning" role="alert">
                                    <i class="fas fa-exclamation-triangle" aria-hidden="true"></i>
                                    ${this.data.cookieGroups[groupIndex].cookieList[index].alertMessage}
                                  </span>
                                </div>`
                              : ''
                          }
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Cookies</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.cookieName
                          }</span></div>
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Vencimento</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.expires
                          }</span></div>
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Domínio</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.domain
                          }</span></div>
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Empresa</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.entreprise
                          }</span></div>
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Finalidade</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.purpose
                          }</span></div>
                        </div>
                        <div class="row">
                          <div class="col-4 col-sm-2 mb-1 cookie-term"><span>Descrição</span></div>
                          <div class="col mb-1 cookie-data"><span>${
                            cookie.description
                          }</span></div>
                        </div>
                      </div>
                    </div>`
    })
    return cookieInfo
  }

  _createSwitchAll(selected) {
    const switchAll = `<div class="br-switch small icon">
                          <input id="switch-all" type="checkbox" ${
                            selected ? 'checked' : ''
                          }>
                          <label for="switch-all">Selecionar Tudo</label>
                        </div>`

    return switchAll
  }
  _createSwitchButton(index, piece, selected) {
    const switchButton = `<div class="br-switch small icon">
                            <input id="switch-${
                              piece + index
                            }" type="checkbox" ${selected ? 'checked' : ''}>
                            <label for="switch-${piece + index}"></label>
                            <div class="switch-data" data-enabled="Ligado" data-disabled="Desligado"></div>
                          </div>`

    return switchButton
  }

  _buildNotificationInfo() {
    let noteInfo = ''
    this.data.noteList.forEach((item) => {
      noteInfo += `<div class="br-item notes">
                    <div class="row">
                      <div class="col">
                        <p>${item.question}</p>
                        <p>${item.answer}</p>
                      </div>
                    </div>
                  </div>`
    })
    return noteInfo
  }

  _buildLinkInfo() {
    let linkInfo = ''
    this.data.links.forEach((link) => {
      linkInfo += `<div class="br-item text-center">
                    <div class="row">
                      <div class="col">
                        <a href="${link.url}">${link.name}<i class="fas fa-external-link-alt" aria-hidden="true"></i>
                        </a>
                      </div>
                    </div>
                  </div>`
    })
    return linkInfo
  }

  _setPriorityValues() {
    if (this.data.selectAll) {
      this.data.cookieGroups.forEach((group) => {
        group.groupSelected = true
        group.cookieList.forEach((cookie) => {
          cookie.cookieSelected = true
        })
      })
    } else {
      this.data.cookieGroups.forEach((group) => {
        if (group.groupSelected) {
          group.cookieList.forEach((cookie) => {
            cookie.cookieSelected = true
          })
        }
      })
    }
  }

  _setConsistency() {
    let allGroupsTrue = true
    this.data.cookieGroups.forEach((group) => {
      let allCookiesTrue = true
      group.cookieList.forEach((cookie) => {
        if (!cookie.cookieSelected) {
          allCookiesTrue = false
        }
      })
      if (allCookiesTrue) {
        group.groupSelected = true
      }
      if (!group.groupSelected) {
        allGroupsTrue = false
      }
    })
    if (allGroupsTrue) {
      this.data.selectAll = true
    }
  }

  _setAllOptOut() {
    if (!this.data.allOptOut) {
      this.data.selectAll = true
      this.data.cookieGroups.forEach((group) => {
        group.groupOptOut = false
        group.groupSelected = true
        group.cookieList.forEach((cookie) => {
          cookie.cookieOptOut = false
          cookie.cookieSelected = true
        })
      })
    }
  }

  _setGroupOptOut() {
    this.data.cookieGroups.forEach((group) => {
      if (!group.groupOptOut) {
        group.groupSelected = true
        group.cookieList.forEach((cookie) => {
          cookie.cookieOptOut = false
          cookie.cookieSelected = true
        })
      }
    })
  }

  _setCookieOptOut() {
    this.data.cookieGroups.forEach((group) => {
      group.cookieList.forEach((cookie) => {
        if (!cookie.cookieOptOut) {
          cookie.cookieSelected = true
        }
      })
    })
  }

  _insertAlertMessage(indexGroup, indexCookie) {
    if (
      this.data.cookieGroups[indexGroup].cookieList[indexCookie].alertMessage &&
      this.data.cookieGroups[indexGroup].cookieList[indexCookie]
        .alertMessage !== ''
    ) {
      const messageTemplate = `<div class="col text-right message">
                                <span class="feedback warning" role="alert">
                                  <i class="fas fa-exclamation-triangle" aria-hidden="true"></i>
                                  ${this.data.cookieGroups[indexGroup].cookieList[indexCookie].alertMessage}
                                </span>
                              </div>`

      for (const [indexGr, group] of this.component
        .querySelectorAll('.main-content .group-info')
        .entries()) {
        if (indexGr === indexGroup) {
          for (const [
            indexCo,
            cookie,
          ] of group.nextElementSibling
            .querySelectorAll('.main-content .cookie-info .br-card')
            .entries()) {
            if (indexCo === indexCookie) {
              const firstRow = cookie.querySelector('.row:nth-child(2)')
              firstRow.insertAdjacentHTML('afterbegin', messageTemplate)
              break
            }
          }
          break
        }
      }
    }
  }

  _removeAlertMessage(indexGroup, indexCookie) {
    for (const [indexGr, group] of this.component
      .querySelectorAll('.main-content .group-info')
      .entries()) {
      if (indexGr === indexGroup) {
        for (const [
          indexCo,
          cookie,
        ] of group.nextElementSibling
          .querySelectorAll('.main-content .cookie-info .br-card')
          .entries()) {
          if (indexCo === indexCookie) {
            const messageCol = cookie.querySelector(
              '.row:nth-child(2) .message'
            )
            if (messageCol) {
              messageCol.remove()
            }
            break
          }
        }
        break
      }
    }
  }

  _setCookieSelection() {
    this.component
      .querySelectorAll(
        '.main-content .header .br-switch input[type="checkbox"]'
      )
      .forEach((switchAll) => {
        switchAll.addEventListener('click', () => {
          this.data.selectAll = switchAll.checked
          if (switchAll.checked) {
            switchAll.nextElementSibling.innerHTML = 'Desselecionar Tudo'
          } else {
            switchAll.nextElementSibling.innerHTML = 'Selecionar Tudo'
          }
          this.component
            .querySelectorAll(
              '.main-content .group-info .br-switch input[type="checkbox"]'
            )
            .forEach((switchGroup) => {
              if (switchGroup.checked !== switchAll.checked) {
                switchGroup.click()
              }
            })
        })
      })

    this.component
      .querySelectorAll('.main-content .group-info')
      .forEach((group, groupIndex) => {
        group
          .querySelectorAll('.br-switch input[type="checkbox"]')
          .forEach((switchGroup) => {
            switchGroup.addEventListener('click', () => {
              this.data.cookieGroups[groupIndex].groupSelected =
                switchGroup.checked
              group.nextElementSibling
                .querySelectorAll('.br-switch input[type="checkbox"]')
                .forEach((switchCookie) => {
                  if (switchCookie.checked !== switchGroup.checked) {
                    switchCookie.click()
                  }
                })
              this.component
                .querySelectorAll(
                  '.main-content .header .br-switch input[type="checkbox"]'
                )
                .forEach((switchAll) => {
                  if (!switchGroup.checked) {
                    if (switchAll.checked) {
                      switchAll.nextElementSibling.innerHTML = 'Selecionar Tudo'
                      switchAll.checked = false
                      this.data.selectAll = false
                    }
                  } else {
                    let allTrue = true
                    this.component
                      .querySelectorAll('.main-content .group-info')
                      .forEach((group) => {
                        group
                          .querySelectorAll('.br-switch input[type="checkbox"]')
                          .forEach((switchItem) => {
                            if (!switchItem.checked) {
                              allTrue = false
                            }
                          })
                      })
                    if (allTrue) {
                      switchAll.click()
                    }
                  }
                })
            })
          })
      })

    this.component
      .querySelectorAll('.main-content .group-info')
      .forEach((group, groupIndex) => {
        group.nextElementSibling
          .querySelectorAll('.br-switch input[type="checkbox"]')
          .forEach((switchCookie, cookieIndex) => {
            switchCookie.addEventListener('click', () => {
              this.data.cookieGroups[groupIndex].cookieList[
                cookieIndex
              ].cookieSelected = switchCookie.checked
              if (switchCookie.checked) {
                this._removeAlertMessage(groupIndex, cookieIndex)
              } else {
                this._insertAlertMessage(groupIndex, cookieIndex)
              }
              group
                .querySelectorAll('.br-switch input[type="checkbox"]')
                .forEach((switchGroup) => {
                  if (!switchCookie.checked) {
                    if (switchGroup.checked) {
                      switchGroup.checked = false
                      this.data.cookieGroups[groupIndex].groupSelected = false
                      this.component
                        .querySelectorAll(
                          '.main-content .header .br-switch input[type="checkbox"]'
                        )
                        .forEach((switchAll) => {
                          if (!switchGroup.checked) {
                            if (switchAll.checked) {
                              switchAll.nextElementSibling.innerHTML =
                                'Selecionar Tudo'
                              switchAll.checked = false
                              this.data.selectAll = false
                            }
                          } else {
                            let allTrue = true
                            this.component
                              .querySelectorAll('.main-content .group-info')
                              .forEach((group) => {
                                group
                                  .querySelectorAll(
                                    '.br-switch input[type="checkbox"]'
                                  )
                                  .forEach((switchItem) => {
                                    if (!switchItem.checked) {
                                      allTrue = false
                                    }
                                  })
                              })
                            if (allTrue) {
                              switchAll.click()
                            }
                          }
                        })
                    }
                  } else {
                    let allTrue = true
                    group.nextElementSibling
                      .querySelectorAll('.br-switch input[type="checkbox"]')
                      .forEach((switchItem) => {
                        if (!switchItem.checked) {
                          allTrue = false
                        }
                      })
                    if (allTrue) {
                      switchGroup.click()
                    }
                  }
                })
            })
          })
      })
  }

  _setSwitchBehavior() {
    const switchAll = this.component.querySelector('#switch-all')
    switchAll.addEventListener('click', () => {
      this.component
        .querySelectorAll(
          '.main-content .group-info .br-switch input[type="checkbox"], .main-content .cookie-info .br-switch input[type="checkbox"]'
        )
        .forEach((switchItem) => {
          if (switchItem.checked !== switchAll.checked) {
            switchItem.click()
          }
        })
    })

    this.component
      .querySelectorAll('.main-content .group-info')
      .forEach((group, indexGroup) => {
        const switchGroup = group.querySelector(
          '.br-switch input[type="checkbox"]'
        )
        if (switchGroup) {
          switchGroup.addEventListener('click', () => {
            group.nextElementSibling
              .querySelectorAll('.br-switch input[type="checkbox"]')
              .forEach((switchCookie) => {
                if (switchCookie.checked !== switchGroup.checked) {
                  switchCookie.click()
                }
              })
            if (switchGroup.checked) {
              if (this._getAllSwitchesState() === true) {
                switchAll.checked = true
                this.data.selectAll = switchAll.checked
              }
            } else {
              switchAll.checked = false
              this.data.selectAll = switchAll.checked
            }
          })

          group.nextElementSibling
            .querySelectorAll('.br-switch input[type="checkbox"]')
            .forEach((switchCookie) => {
              switchCookie.addEventListener('click', () => {
                if (switchCookie.checked) {
                  if (this._getAllGroupSwitchesState(group) === true) {
                    switchGroup.checked = true
                    this.data.cookieGroups[indexGroup].groupSelected =
                      switchGroup.checked
                    if (this._getAllSwitchesState() === true) {
                      switchAll.checked = true
                      this.data.selectAll = switchAll.checked
                    }
                  }
                } else {
                  switchGroup.checked = false
                  this.data.cookieGroups[indexGroup].groupSelected =
                    switchGroup.checked
                  switchAll.checked = false
                  this.data.selectAll = switchAll.checked
                }
              })
            })
        }
      })
  }

  _getAllSwitchesState() {
    let state = true
    this.component
      .querySelectorAll(
        '.main-content .group-info .br-switch input[type="checkbox"], .main-content .cookie-info .br-switch input[type="checkbox"]'
      )
      .forEach((item) => {
        if (!item.checked) {
          state = false
        }
      })
    return state
  }

  _getAllGroupSwitchesState(group) {
    let state = true
    group.nextElementSibling
      .querySelectorAll('.br-switch input[type="checkbox"]')
      .forEach((item) => {
        if (!item.checked) {
          state = false
        }
      })
    return state
  }

  _setGroupBehavior() {
    this.component
      .querySelectorAll('.main-content .br-item .br-button')
      .forEach((button) => {
        button.addEventListener('click', () => {
          let element = button
          const icon = button.querySelector('i.fas')
          while (!element.classList.contains('br-item')) {
            element = element.parentNode
          }
          if (element.classList.contains('open')) {
            element.classList.remove('open')
            icon.classList.remove('fa-angle-up')
            icon.classList.add('fa-angle-down')
          } else {
            element.classList.add('open')
            icon.classList.remove('fa-angle-down')
            icon.classList.add('fa-angle-up')
          }
        })
      })
  }

  _setAcceptBehavior() {
    const acceptButton = this.component.querySelector(
      '.actions .br-button.primary'
    )
    acceptButton.addEventListener('click', () => {
      this.callback(this._setOutputJSON())
    })
  }

  _setOutputJSON() {
    this.output = {}
    this.output.selectAll = this.data.selectAll
    this.output.cookieGroups = []
    this.data.cookieGroups.forEach((group) => {
      const cookies = []
      group.cookieList.forEach((cookie) => {
        cookies.push({
          cookieId: cookie.cookieId,
          cookieName: cookie.cookieName,
          cookieSelected: cookie.cookieSelected,
        })
      })
      this.output.cookieGroups.push({
        groupId: group.groupId,
        groupName: group.groupName,
        groupSelected: group.groupSelected,
        cookieList: cookies,
      })
    })
    return JSON.stringify(this.output)
  }
}

const cookiebarData = [
  {
    lang: 'pt-br',
    allOptOut: true,
    acceptButton: 'Aceitar',
    optInButton: 'Ver Política de Cookies',
    infoText: 'Minim pariatur amet laboris sint consectetur enim do voluptate',
    mainTitle: 'Exercitation et proident',
    lastUpdate: '01/02/2021',
    entryText:
      'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Doloribus aspernatur neque culpa nisi alias. Voluptatem dicta nihil magnam, cumque voluptatum animi distinctio molestias recusandae ipsam, sapiente unde error repellendus quibusdam?',
    selectAll: false,
    cookieGroups: [
      {
        groupId: 'necessarios',
        groupName: 'Estritamente necessários',
        groupOptOut: true,
        groupSelected: false,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'necessario-1',
            cookieOptOut: true,
            cookieSelected: false,
            alertMessage: 'Alerta group 0 - cookie 0',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'necessario-2',
            cookieOptOut: true,
            cookieSelected: false,
            alertMessage: 'Alerta group 0 - cookie 1',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
      {
        groupId: 'desempenho',
        groupName: 'Desempenho, funcionamento, marketing e personalização',
        groupOptOut: true,
        groupSelected: false,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'desempenho-2',
            cookieOptOut: true,
            cookieSelected: false,
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'desempenho-2',
            cookieOptOut: true,
            cookieSelected: true,
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
      {
        groupId: 'experiencia',
        groupName: 'Experiência do site',
        groupOptOut: true,
        groupSelected: false,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'experiencia-1',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage: 'Alerta group 2 - cookie 0',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'experiencia-2',
            cookieOptOut: true,
            cookieSelected: true,
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
    ],
    noteTitle: 'Aviso sobre cookies',
    noteList: [
      {
        question: 'O que são cookies?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Durabilidade?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Proveniência?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Finalidade?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
    ],
    links: [
      {
        name:
          'Declaração de Conformidade com os Princípios de Proteção de Dados',
        url: '#',
      },
    ],
  },
  {
    lang: 'en',
    allOptOut: true,
    infoText: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit.',
    mainTitle: 'Respeitamos a sua Privacidade',
    lastUpdate: '01/02/2021',
    entryText:
      'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt culpa corrupti quia minus ullam veniam odit, deleniti reiciendis voluptatum officiis adipisci, commodi perspiciatis aspernatur, libero ratione. Molestias vero accusamus sapiente!',
    selectAll: false,
    cookieGroups: [
      {
        groupId: 'necessarios',
        groupName: 'Estritamente necessários',
        groupOptOut: true,
        groupSelected: false,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'necessario-1',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'necessario-2',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
      {
        groupId: 'desempenho',
        groupName: 'Desempenho, funcionamento, marketing e personalização',
        groupOptOut: true,
        groupSelected: false,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'desempenho-1',
            cookieOptOut: true,
            cookieSelected: false,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'desempenho-2',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
      {
        groupId: 'experiencia',
        groupName: 'Experiência do site',
        groupOptOut: true,
        groupSelected: true,
        groupText:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum delectus fuga omnis, placeat harum id aliquam, blanditiis consectetur est cupiditate ipsam alias vitae veritatis beatae, aperiam totam assumenda. Sed, modi!',
        cookieList: [
          {
            cookieId: 'experiencia-1',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
          {
            cookieId: 'experiencia-2',
            cookieOptOut: true,
            cookieSelected: true,
            alertMessage:
              'Ao clicar nessa opção sua navegação ficará comprometida',
            cookieName: 'optimizelyEndUserId',
            expires: '30 minutos',
            domain: 'serpro.gov.br',
            entreprise: 'Serpro',
            purpose: 'Autorização',
            description:
              'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui numquam inventore fuga consectetur minus accusantium sapiente, distinctio dolorum illum, doloremque rem deleniti recusandae quod rerum quidem amet? Unde, laudantium cum.',
          },
        ],
      },
    ],
    noteTitle: 'Aviso sobre cookies',
    noteList: [
      {
        question: 'O que são cookies?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Durabilidade?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Proveniência?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
      {
        question: 'Finalidade?',
        answer:
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eius distinctio rerum ad, maxime alias vel minima, asperiores sequi eveniet non optio officiis quaerat reiciendis quae odio explicabo ut debitis?',
      },
    ],
    links: [
      {
        name:
          'Declaração de Conformidade com os Princípios de Proteção de Dados',
        url: '#',
      },
    ],
  },
]

function callback(json) {
  // console.log(json)
}

// new BRCookiebar
const cookiebarList = []
for (const brCookiebar of window.document.querySelectorAll('.br-cookiebar')) {
  cookiebarList.push(
    new BRCookiebar(
      'br-cookiebar',
      brCookiebar,
      JSON.stringify(cookiebarData),
      'pt-br',
      callback
    )
  )
}
/* harmony default export */ __webpack_exports__["default"] = (BRCookiebar);


/***/ }),

/***/ 158:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(10);
__webpack_require__(47);
__webpack_require__(48);
module.exports = __webpack_require__(159);


/***/ }),

/***/ 159:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/cookiebar/examples/cookiebar-padrao.html");

/***/ }),

/***/ 47:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 48:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/cookiebar/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=cookiebar.js.map