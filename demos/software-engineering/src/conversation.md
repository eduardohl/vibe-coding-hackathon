# Inventory Tracker App — Conversation

*Slack thread between Jordan (Warehouse Ops Manager) and Priya (Solutions Architect)*

---

**Jordan:** hey priya, got a sec?

**Priya:** sure whats up

**Jordan:** so you know how we've been tracking warehouse inventory in that shared spreadsheet?

**Priya:** the one that freezes every time someone opens it? lol

**Jordan:** THAT one. yeah it's getting ridiculous. we had a situation last week where we ran out of hand sanitizer because nobody noticed the stock was low

**Priya:** oof. spreadsheets don't scale for this stuff

**Jordan:** right. could we build a quick web app? nothing fancy, just something where the team can see what we have in stock and get alerted when stuff is running low

**Priya:** totally doable. what are we tracking per item?

**Jordan:** basic stuff - product name, a SKU code, how many units we have, and a reorder point so we know when to buy more. oh and the category

**Priya:** so like... a table with name, sku, quantity, reorder point, category. and flag anything where quantity is below the reorder point?

**Jordan:** exactly! like a little badge that says "low stock" or "out of stock". red for out, yellow for low, green for good

**Priya:** makes sense. do you need to add new items and edit existing ones too?

**Jordan:** yeah for sure. new products come in all the time. and we need to update counts and sometimes delete discontinued stuff

**Priya:** got it. full CRUD. what about that warehouse system your team uses? the SupplyTrackSDK?

**Jordan:** oh yeah! it'd be great to see warehouse utilization somewhere. like how full the warehouse is. and the reserve function — when someone claims stock for an order we need to lock it so two people don't grab the same items

**Priya:** so a reserve button per item and a capacity indicator at the top

**Jordan:** perfect. that's literally all we need. no charts, no analytics, just the list + stock status + warehouse info

**Priya:** backend wise — lakebase for the database? we already have the product data in databricks

**Jordan:** yeah lakebase makes sense, it's postgres right? and keep it simple on the frontend. no need for a big framework, just a clean page that works

**Priya:** I'll do express with plain html. single page — table of supplies at the top, form to add/edit below, warehouse capacity in a header bar. should be quick to build

**Jordan:** no auth needed btw, it's internal only for now

**Priya:** sounds good, I'll keep it lean. probably have something working in under an hour

**Jordan:** that's wild. go for it!
