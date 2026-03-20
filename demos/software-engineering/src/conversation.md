# Inventory Tracker App — Conversation

*Slack thread between Jordan (Warehouse Ops Manager) and Priya (Solutions Architect)*

---

**Jordan:** hey priya, you around?

**Priya:** yep whats up

**Jordan:** ok so remember that giant spreadsheet we use to track warehouse inventory?

**Priya:** the google sheet that takes 45 seconds to load? how could i forget

**Jordan:** lmao yeah that one. so last tuesday we completely ran out of hand sanitizer. like zero units. nobody caught it because the sheet was showing stale numbers from the week before

**Priya:** yikes

**Jordan:** and then marcus tried to order more but didn't realize someone else already placed an order for the same thing. so now we have 400 cases of hand sanitizer arriving next week

**Priya:** classic spreadsheet problem. no real-time visibility, no coordination

**Jordan:** exactly. so i'm wondering... could we throw together a simple web app? like really simple. i just need the team to be able to pull it up and see what we actually have in stock right now

**Priya:** yeah absolutely. what info do you need per product?

**Jordan:** uhhh let me think. the product name obviously, the sku, how many units we currently have, and then a reorder point — like a threshold where if we drop below it, the app yells at us. oh and what department or category it belongs to

**Priya:** so name, sku, quantity on hand, reorder point, and category. and you want some kind of visual indicator when quantity drops below the reorder point?

**Jordan:** yes!! like color coded. green means we're good, yellow means we're getting low, red means we're out. something you can glance at and immediately know what needs attention

**Priya:** love it. and i'm guessing you need to be able to add new products when they come in? edit quantities?

**Jordan:** yep. and delete stuff we discontinue. the usual add/edit/delete

**Priya:** cool. for the database i'm thinking lakebase since we already have our product catalog in databricks. it's postgres under the hood so super easy to query from node

**Jordan:** perfect yeah that works

**Priya:** i'll keep the frontend dead simple — plain html, no fancy frameworks. one page with the inventory table, a form to add or edit items, and maybe a status bar at the top showing how many items are low or out of stock

**Jordan:** that's exactly what i want. oh one more thing — no login or anything. this is just for our internal warehouse team

**Priya:** done. i'll have something running today

**Jordan:** you're a legend
