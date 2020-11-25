const staticAsserts = [
  '../../static/fmapbox.geojson',
  '../../static/materialize/css/index.css',
  '../../static/materialize/css/materialize.min.css',
  '../../static/materialize/css/map/map.css',
  '../../static/materialize/css/map/additionalMapStyle.css',
  '../../static/materialize/js/index.js',
  '../../static/materialize/js/materialize.min.js',
  '../../static/materialize/js/map/map.js',
  '../../static/materialize/js/map/additionalMapStyle.js'
];


self.addEventListener('install', async event => {
  const cache = await caches.open('static')
  cache.addAll(staticAsserts)
});

self.addEventListener('fetch', event => {
  const req = event.request;
  const url = new URL(req.url);

  if (url.origin === location.origin) {
    event.respondWith(cacheFirst(req));
  } else {
    event.respondWith(networkFist(req));
  }
});

async function cacheFirst(req) {
  const cachedResponse = await caches.match(req);
  return cachedResponse || fetch(req);
}

async function networkFist(req) {
  const cache = await caches.open('dynamic');

  try {
    const res = await fetch(req);
    cache.put(req, res.clone());
    return res;
  } catch(error) {
    const cachedResponse = await cache.match(req);
    return cachedResponse || "ups"
  }
}