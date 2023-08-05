import { r as react } from './index-6ed86a98.js';
import { r as reactDom } from './index-21e68f69.js';
import { h as htm } from './htm.module-dd7abb54.js';
import { j as jsonpatch } from './index-6ddd8323.js';

function serializeEvent(event) {
  const data = {};

  if (event.type in eventTransforms) {
    Object.assign(data, eventTransforms[event.type](event));
  }

  const target = event.target;
  if (target.tagName in targetTransforms) {
    targetTransforms[target.tagName].forEach((trans) =>
      Object.assign(data, trans(target))
    );
  }

  return data;
}

const targetTransformCategories = {
  hasValue: (target) => ({
    value: target.value,
  }),
  hasCurrentTime: (target) => ({
    currentTime: target.currentTime,
  }),
  hasFiles: (target) => {
    if (target?.type == "file") {
      return {
        files: Array.from(target.files).map((file) => ({
          lastModified: file.lastModified,
          name: file.name,
          size: file.size,
          type: file.type,
        })),
      };
    } else {
      return {};
    }
  },
};

const targetTagCategories = {
  hasValue: ["BUTTON", "INPUT", "OPTION", "LI", "METER", "PROGRESS", "PARAM"],
  hasCurrentTime: ["AUDIO", "VIDEO"],
  hasFiles: ["INPUT"],
};

const targetTransforms = {};

Object.keys(targetTagCategories).forEach((category) => {
  targetTagCategories[category].forEach((type) => {
    const transforms = targetTransforms[type] || (targetTransforms[type] = []);
    transforms.push(targetTransformCategories[category]);
  });
});

const eventTransformCategories = {
  clipboard: (event) => ({
    clipboardData: event.clipboardData,
  }),
  composition: (event) => ({
    data: event.data,
  }),
  keyboard: (event) => ({
    altKey: event.altKey,
    charCode: event.charCode,
    ctrlKey: event.ctrlKey,
    key: event.key,
    keyCode: event.keyCode,
    locale: event.locale,
    location: event.location,
    metaKey: event.metaKey,
    repeat: event.repeat,
    shiftKey: event.shiftKey,
    which: event.which,
  }),
  mouse: (event) => ({
    altKey: event.altKey,
    button: event.button,
    buttons: event.buttons,
    clientX: event.clientX,
    clientY: event.clientY,
    ctrlKey: event.ctrlKey,
    metaKey: event.metaKey,
    pageX: event.pageX,
    pageY: event.pageY,
    screenX: event.screenX,
    screenY: event.screenY,
    shiftKey: event.shiftKey,
  }),
  pointer: (event) => ({
    pointerId: event.pointerId,
    width: event.width,
    height: event.height,
    pressure: event.pressure,
    tiltX: event.tiltX,
    tiltY: event.tiltY,
    pointerType: event.pointerType,
    isPrimary: event.isPrimary,
  }),
  selection: () => {
    return { selectedText: window.getSelection().toString() };
  },
  touch: (event) => ({
    altKey: event.altKey,
    ctrlKey: event.ctrlKey,
    metaKey: event.metaKey,
    shiftKey: event.shiftKey,
  }),
  ui: (event) => ({
    detail: event.detail,
  }),
  wheel: (event) => ({
    deltaMode: event.deltaMode,
    deltaX: event.deltaX,
    deltaY: event.deltaY,
    deltaZ: event.deltaZ,
  }),
  animation: (event) => ({
    animationName: event.animationName,
    pseudoElement: event.pseudoElement,
    elapsedTime: event.elapsedTime,
  }),
  transition: (event) => ({
    propertyName: event.propertyName,
    pseudoElement: event.pseudoElement,
    elapsedTime: event.elapsedTime,
  }),
};

const eventTypeCategories = {
  clipboard: ["copy", "cut", "paste"],
  composition: ["compositionend", "compositionstart", "compositionupdate"],
  keyboard: ["keydown", "keypress", "keyup"],
  mouse: [
    "click",
    "contextmenu",
    "doubleclick",
    "drag",
    "dragend",
    "dragenter",
    "dragexit",
    "dragleave",
    "dragover",
    "dragstart",
    "drop",
    "mousedown",
    "mouseenter",
    "mouseleave",
    "mousemove",
    "mouseout",
    "mouseover",
    "mouseup",
  ],
  pointer: [
    "pointerdown",
    "pointermove",
    "pointerup",
    "pointercancel",
    "gotpointercapture",
    "lostpointercapture",
    "pointerenter",
    "pointerleave",
    "pointerover",
    "pointerout",
  ],
  selection: ["select"],
  touch: ["touchcancel", "touchend", "touchmove", "touchstart"],
  ui: ["scroll"],
  wheel: ["wheel"],
  animation: ["animationstart", "animationend", "animationiteration"],
  transition: ["transitionend"],
};

const eventTransforms = {};

Object.keys(eventTypeCategories).forEach((category) => {
  eventTypeCategories[category].forEach((type) => {
    eventTransforms[type] = eventTransformCategories[category];
  });
});

function applyPatchInplace(doc, pathPrefix, patch) {
  if (pathPrefix) {
    patch = patch.map((op) =>
      Object.assign({}, op, { path: pathPrefix + op.path })
    );
  }
  jsonpatch.applyPatch(doc, patch, false, true);
}

const html = htm.bind(react.createElement);
const LayoutConfigContext = react.createContext({
  sendEvent: undefined,
  loadImportSource: undefined,
});

function Layout({ saveUpdateHook, sendEvent, loadImportSource }) {
  const [model, patchModel] = useInplaceJsonPatch({});

  react.useEffect(() => saveUpdateHook(patchModel), [patchModel]);

  if (model.tagName) {
    return html`
      <${LayoutConfigContext.Provider} value=${{ sendEvent, loadImportSource }}>
        <${Element} model=${model} />
      <//>
    `;
  } else {
    return html`<div />`;
  }
}

function Element({ model }) {
  if (model.importSource) {
    return html`<${ImportedElement} model=${model} />`;
  } else {
    return html`<${StandardElement} model=${model} />`;
  }
}

function StandardElement({ model }) {
  const config = react.useContext(LayoutConfigContext);
  const children = elementChildren(model.children);
  const attributes = elementAttributes(model, config.sendEvent);
  // Use createElement here to avoid warning about variable numbers of children not
  // having keys. Warning about this must now be the responsibility of the server
  // providing the models instead of the client rendering them.
  return react.createElement(model.tagName, attributes, ...children);
}

function ImportedElement({ model }) {
  const config = react.useContext(LayoutConfigContext);

  const importSourceFallback = model.importSource.fallback;
  const [importSource, setImportSource] = react.useState(null);

  if (!importSource) {
    // load the import source in the background
    loadImportSource(config, model.importSource).then(setImportSource);

    // display a fallback if one was given
    if (!importSourceFallback) {
      return html`<div />`;
    } else if (typeof importSourceFallback == "string") {
      return html`<div>${importSourceFallback}</div>`;
    } else {
      return html`<${StandardElement} model=${importSourceFallback} />`;
    }
  } else {
    return html`<${RenderImportedElement}
      model=${model}
      importSource=${importSource}
    />`;
  }
}

function RenderImportedElement({ model, importSource }) {
  const config = react.useContext(LayoutConfigContext);
  const mountPoint = react.useRef(null);
  const sourceBinding = react.useRef(null);

  react.useEffect(() => {
    sourceBinding.current = importSource.bind(mountPoint.current);
    if (!importSource.data.unmountBeforeUpdate) {
      return sourceBinding.current.unmount;
    }
  }, []);

  // this effect must run every time in case the model has changed
  react.useEffect(() => {
    sourceBinding.current.render(model);
    if (importSource.data.unmountBeforeUpdate) {
      return sourceBinding.current.unmount;
    }
  });

  return html`<div ref=${mountPoint} />`;
}

function elementChildren(modelChildren) {
  if (!modelChildren) {
    return [];
  } else {
    return modelChildren.map((child) => {
      switch (typeof child) {
        case "object":
          return html`<${Element} key=${child.key} model=${child} />`;
        case "string":
          return child;
      }
    });
  }
}

function elementAttributes(model, sendEvent) {
  const attributes = Object.assign({}, model.attributes);

  if (model.eventHandlers) {
    for (const [eventName, eventSpec] of Object.entries(model.eventHandlers)) {
      attributes[eventName] = eventHandler(sendEvent, eventSpec);
    }
  }

  return attributes;
}

function eventHandler(sendEvent, eventSpec) {
  return function () {
    const data = Array.from(arguments).map((value) => {
      if (typeof value === "object" && value.nativeEvent) {
        if (eventSpec["preventDefault"]) {
          value.preventDefault();
        }
        if (eventSpec["stopPropagation"]) {
          value.stopPropagation();
        }
        return serializeEvent(value);
      } else {
        return value;
      }
    });
    sendEvent({
      data: data,
      target: eventSpec["target"],
    });
  };
}

function loadImportSource(config, importSource) {
  return config
    .loadImportSource(importSource.source, importSource.sourceType)
    .then((module) => {
      if (typeof module.bind == "function") {
        return {
          data: importSource,
          bind: (node) => {
            const binding = module.bind(node, config);
            if (
              typeof binding.render == "function" &&
              typeof binding.unmount == "function"
            ) {
              return {
                render: (model) => {
                  binding.render(
                    module[model.tagName],
                    elementAttributes(model, config.sendEvent),
                    model.children
                  );
                },
                unmount: binding.unmount,
              };
            } else {
              console.error(
                `${importSource.source} returned an impropper binding`
              );
            }
          },
        };
      } else {
        console.error(
          `${importSource.source} did not export a function 'bind'`
        );
      }
    });
}

function useInplaceJsonPatch(doc) {
  const ref = react.useRef(doc);
  const forceUpdate = useForceUpdate();

  const applyPatch = react.useCallback(
    (path, patch) => {
      applyPatchInplace(ref.current, path, patch);
      forceUpdate();
    },
    [ref, forceUpdate]
  );

  return [ref.current, applyPatch];
}

function useForceUpdate() {
  const [, updateState] = react.useState();
  return react.useCallback(() => updateState({}), []);
}

function mountLayout(mountElement, layoutProps) {
  reactDom.render(react.createElement(Layout, layoutProps), mountElement);
}

function mountLayoutWithWebSocket(
  element,
  endpoint,
  loadImportSource,
  maxReconnectTimeout
) {
  mountLayoutWithReconnectingWebSocket(
    element,
    endpoint,
    loadImportSource,
    maxReconnectTimeout
  );
}

function mountLayoutWithReconnectingWebSocket(
  element,
  endpoint,
  loadImportSource,
  maxReconnectTimeout,
  mountState = {
    everMounted: false,
    reconnectAttempts: 0,
    reconnectTimeoutRange: 0,
  }
) {
  const socket = new WebSocket(endpoint);

  const updateHookPromise = new LazyPromise();

  socket.onopen = (event) => {
    console.log(`Connected.`);

    if (mountState.everMounted) {
      reactDom.unmountComponentAtNode(element);
    }
    _resetOpenMountState(mountState);

    mountLayout(element, {
      loadImportSource,
      saveUpdateHook: updateHookPromise.resolve,
      sendEvent: (event) => socket.send(JSON.stringify(event)),
    });
  };

  socket.onmessage = (event) => {
    const [pathPrefix, patch] = JSON.parse(event.data);
    updateHookPromise.promise.then((update) => update(pathPrefix, patch));
  };

  socket.onclose = (event) => {
    if (!maxReconnectTimeout) {
      console.log(`Connection lost.`);
      return;
    }

    const reconnectTimeout = _nextReconnectTimeout(
      maxReconnectTimeout,
      mountState
    );

    console.log(`Connection lost, reconnecting in ${reconnectTimeout} seconds`);

    setTimeout(function () {
      mountState.reconnectAttempts++;
      mountLayoutWithReconnectingWebSocket(
        element,
        endpoint,
        loadImportSource,
        maxReconnectTimeout,
        mountState
      );
    }, reconnectTimeout * 1000);
  };
}

function _resetOpenMountState(mountState) {
  mountState.everMounted = true;
  mountState.reconnectAttempts = 0;
  mountState.reconnectTimeoutRange = 0;
}

function _nextReconnectTimeout(maxReconnectTimeout, mountState) {
  const timeout =
    Math.floor(Math.random() * mountState.reconnectTimeoutRange) || 1;
  mountState.reconnectTimeoutRange =
    (mountState.reconnectTimeoutRange + 5) % maxReconnectTimeout;
  if (mountState.reconnectAttempts == 4) {
    window.alert(
      "Server connection was lost. Attempts to reconnect are being made in the background."
    );
  }
  return timeout;
}

function LazyPromise() {
  this.promise = new Promise((resolve, reject) => {
    this.resolve = resolve;
    this.reject = reject;
  });
}

export { mountLayoutWithWebSocket as m };
