/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "bmrflcu0t4ljh70",
    "created": "2023-10-14 19:46:37.789Z",
    "updated": "2023-10-14 19:46:37.789Z",
    "name": "Blacklist",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "blqsjtbr",
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
  const collection = dao.findCollectionByNameOrId("bmrflcu0t4ljh70");

  return dao.deleteCollection(collection);
})
