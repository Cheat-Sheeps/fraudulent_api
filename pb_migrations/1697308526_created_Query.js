/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "hj31bonr3r6z96e",
    "created": "2023-10-14 18:35:26.886Z",
    "updated": "2023-10-14 18:35:26.886Z",
    "name": "Query",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "1hjxrxfl",
        "name": "query",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "ivjnyv3p",
        "name": "is_phishing",
        "type": "bool",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {}
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
  const collection = dao.findCollectionByNameOrId("hj31bonr3r6z96e");

  return dao.deleteCollection(collection);
})
