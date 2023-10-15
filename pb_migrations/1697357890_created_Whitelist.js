/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "vjv866izbttcfv3",
    "created": "2023-10-15 08:18:10.583Z",
    "updated": "2023-10-15 08:18:10.583Z",
    "name": "Whitelist",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "a5skohzg",
        "name": "domain",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("vjv866izbttcfv3");

  return dao.deleteCollection(collection);
})
