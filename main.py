def acceptAnswer(numChoices):
  invalidAnswer = True
  stringAnswer = input()
  while invalidAnswer:
    try:
      intAnswer = int(stringAnswer)
    except ValueError:
      print(f"Invalid Choice. Enter a number between 1 and {numChoices}")
      stringAnswer = input()
    else:
      try:
        if intAnswer in range(1, numChoices + 1):
          invalidAnswer = False
          return intAnswer
        else:
          raise TypeError()
      except TypeError:
        print(f"Invalid Choice. Enter a number between 1 and {numChoices}")
        stringAnswer = input()

print('''
Welcome to the mysterious world of "The Enchanted Forest"! You find yourself standing at the edge of a dense forest, its towering trees shrouded in an ethereal mist. A sense of adventure stirs within you as you contemplate the untold secrets that lie within. The air is filled with a strange energy, crackling with possibilities.

To embark on this extraordinary journey, you must make a crucial decision. Will you venture deep into the heart of the forest, or turn back and seek a safer path? The choice is yours to make, and it will shape the course of your adventure.

If you choose to enter the forest and unravel its mysteries, enter 1.
If you decide to turn back and explore elsewhere, turn to page 2.

Remember, every decision you make carries consequences, and the outcome of your adventure lies in your hands. So, are you ready to take the first step into "The Enchanted Forest"? Choose wisely and let the tale unfold!''')
choice1 = acceptAnswer(2)

#LEVEL 1
if choice1 == 1:
  print('''
  Excellent choice! With a courageous spirit, you take a step forward and push through the thick foliage, immersing yourself in the enchantment of the forest. The moment you enter, the atmosphere changes. The air is cooler, and a gentle breeze rustles the leaves above you.

As you delve deeper into the forest, you notice an array of vibrant colors painted across the landscape. Lush greenery blankets the forest floor, interspersed with delicate wildflowers of every hue. Sunlight filters through the dense canopy, casting dappled shadows on the moss-covered ground.

As you wander along the winding path, you stumble upon a peculiar signpost. It points in multiple directions, each marked with intriguing symbols. One path shows an image of a majestic waterfall, suggesting a hidden oasis. Another path displays a crescent moon, hinting at a mystical clearing. The last path bears a depiction of a towering mountain, promising breathtaking views.

Now, it's time to make another decision. Which path will you choose to follow?

If you decide to follow the path to the waterfall, enter 1.
If you choose to follow the path to the mystical clearing, enter 2.
If you opt for the path leading to the mountain, enter 3.

Remember, the forest holds both wonders and challenges, and your choice will determine the course of your adventure. Trust your instincts, and let fate guide you deeper into "The Enchanted Forest."''')
  choice2 = acceptAnswer(3)

  #LEVEL 2
  if choice2 == 1:
    print('''
    The sound of rushing water grows louder as you make your way deeper into the forest.

The path meanders through a thick grove of ancient trees, their gnarled branches reaching towards the sky. Rays of sunlight filter through the dense foliage, creating an enchanting play of light and shadow on the forest floor. The air is filled with a refreshing mist, hinting at the proximity of the waterfall.

As you round a bend in the path, the sight that greets your eyes takes your breath away. A magnificent waterfall cascades down a rocky cliff face, its crystal-clear water sparkling in the sunlight. The sound of the rushing water is both soothing and invigorating, drawing you closer.

At the base of the waterfall, you notice a small, moss-covered stone bridge that crosses a narrow stream. It seems to invite you to explore further. However, you also spot a hidden cave entrance behind the waterfall, concealed by a shimmering curtain of water.

Now, it's time to make another decision. Will you cross the bridge and see where it leads, or will you venture behind the waterfall into the mysterious cave?

If you choose to cross the bridge, enter 1.
If you decide to venture behind the waterfall into the cave, enter 2.

Remember, the forest holds both beauty and mystery, and each choice you make will shape your unique adventure in "The Enchanted Forest." Trust your instincts and let the magic guide you.''')
    choice3 = acceptAnswer(2)

    #LEVEL 3
    if choice3 == 1:
      print('''
      As you approach the small, moss-covered stone bridge at the base of the waterfall, you can't help but feel a sense of anticipation. The rushing water below adds an element of excitement to your journey. With cautious steps, you begin to cross the bridge, the sound of your footsteps echoing in the serene surroundings.

However, just as you reach the midpoint of the bridge, a loud crack pierces the air. Panic sets in as the bridge gives way beneath you, leaving you suspended in mid-air for a brief moment before gravity takes hold. You plunge into the icy waters below with a splash, the world around you turning into a whirl of bubbles and darkness.

ENDING: A bridge's demise''')
    #LEVEL 3
    elif choice3 == 2:
      print('''
      As you step behind the shimmering curtain of water, you enter the hidden cave behind the waterfall. The sound of rushing water fades, replaced by a hushed stillness. The cave is dimly lit, with the soft glow of luminescent moss illuminating the path ahead.

As you explore deeper into the cave, you begin to hear faint echoes of laughter and conversation. Intrigued, you follow the sounds and soon discover a hidden chamber within the cave. To your surprise, it is bustling with activity and populated by a village of cavemen.

The cavemen, with their rugged features and primitive attire, welcome you with open arms. They seem to have established a harmonious existence within the cave, with a well-organized community and a deep sense of camaraderie. Their wisdom and resourcefulness are evident as they navigate their lives in this secluded sanctuary.

Recognizing your curiosity and potential, the cavemen adopt you as one of their own. They teach you their ways, sharing their knowledge of survival, ancient rituals, and the wisdom passed down through generations. You become a valued member of the community, embraced by the warmth and support of your new family.

Together, you explore the depths of the cave, uncovering hidden chambers filled with ancient artifacts and symbols that hint at a rich history and mysticism. The cavemen guide you through their rituals and ceremonies, fostering a deep connection to the natural world and the spiritual forces that reside within it.

As time passes, you flourish in this unique environment, your bond with the cavemen growing stronger. You learn the art of survival, the secrets of the cave, and the profound wisdom that their way of life holds. You find fulfillment and purpose alongside your newfound family, embracing a life of simplicity and connection to the earth.

In the embrace of the cave and the love of the cavemen, you have found a home and a sense of belonging that you never imagined possible.

ENDING: The Hidden Sanctuary''')
  #LEVEL 2
  elif choice2 == 2:
    print('''
    With a sense of intrigue, you choose to follow the path that leads to the mystical clearing. As you walk, the atmosphere around you seems to change. The air becomes lighter, and a gentle breeze carries whispers of ancient secrets.

After a short walk, you emerge from the dense foliage into a small, sunlit clearing. The space is bathed in a soft, golden glow that seems to emanate from the very ground beneath your feet. Vibrant wildflowers bloom in a kaleidoscope of colors, their sweet fragrance filling the air.

In the center of the clearing, you notice an intricately carved stone pedestal. Resting atop it is a small, ornate silver amulet, glimmering with a mysterious radiance. It beckons to you, seemingly calling out to be discovered.

Filled with curiosity, you reach out to touch the amulet. As your fingertips make contact, a surge of energy courses through your body. The world around you begins to spin, and your vision blurs. Overwhelmed by the sudden intensity, you feel your strength wane, and darkness creeps into the edges of your consciousness.

Overwhelmed by the mystical energy of the amulet, you fainted.

ENDING: Curiosity killed the cat''')
  #LEVEL 2
  elif choice2 == 3:
    print('''
    With a sense of adventure and a desire for breathtaking views, you decide to follow the path that leads to the towering mountain. As you make your way through the forest, the air becomes crisper, and the sounds of nature grow more distant.

The path gradually ascends, winding its way up the mountainside. The forest thins, and you begin to catch glimpses of the vast landscape stretching out before you. The distant peaks are shrouded in mist, adding an aura of mystery to the scene.

As you continue your ascent, the terrain becomes steeper, and you find yourself navigating rocky outcrops and narrow ledges. The path demands your attention and surefootedness, but the promise of reaching the mountaintop keeps you going.

After what feels like an arduous climb, you finally reach a plateau. The view that unfolds before your eyes is nothing short of awe-inspiring. Snow-capped peaks pierce the sky, and a sea of clouds blankets the valleys below. The air is thin and crisp, invigorating your senses.

At the edge of the plateau, you spot a weathered stone altar adorned with offerings left by previous travelers. It seems to be a place of reverence, a point of connection between the earthly realm and the vastness of the mountains.

Now, it's time to make another decision. Will you take a moment to rest and reflect at the stone altar, or will you continue your ascent, pushing further into the heights of the mountain?

If you decide to rest and reflect at the stone altar, enter 1.
If you choose to continue your ascent, enter 2.

Remember, the mountain holds both challenges and rewards. Listen to the whispers of the wind and follow your intuition as you navigate through "The Enchanted Forest."''')
    choice3 = acceptAnswer(2)

    #LEVEL 3
    if choice3 == 1:
      print('''
      Feeling a sense of reverence and curiosity, you decide to take a moment to rest and reflect at the stone altar in the mountain plateau. The altar stands as a solemn testament to the connection between the earthly realm and the vastness of the mountains.

As you sit before the weathered stone altar, you close your eyes and take deep breaths, allowing the energy of the mountain to envelop you. In this stillness, you open yourself to the whispers of the ancient forces that reside within the rugged peaks.

As minutes turn into moments, you begin to sense a subtle shift in the air. A surge of power courses through your veins, awakening dormant abilities within you. It is as if the mountain itself has bestowed upon you a gift, granting you great power and unlocking the depths of your potential.

With newfound clarity and a surge of energy, you rise from the stone altar, feeling the weight of the mountain's ancient wisdom and strength within you. As you step away, the world around you takes on a vibrant aura, with sights and sounds heightened by your enhanced perception.

You realize that you now possess the ability to harness the elements, to command the forces of nature, and to shape reality itself. The mountain has gifted you with extraordinary power, and it is up to you to decide how to wield it.

With a mix of awe and determination, you set off from the mountain plateau, embarking on a journey that will reshape the course of your destiny. The world awaits your presence, and the power you now possess will shape the lives of those you encounter.

ENDING: The Mountain's Gift''')
    #LEVEL 3
    elif choice3 == 2:
      print('''
      Driven by a sense of adventure and a desire to conquer the mountain, you decide to continue your ascent without stopping at the stone altar. You feel a surge of determination as you press forward, eager to reach the summit and witness the breathtaking views that await.

The path becomes steeper, and the air grows thinner as you ascend higher. Your muscles ache, and your breath becomes more labored, but you push through the physical challenges. The mountain seems to test your resolve, yet you remain steadfast in your pursuit.

As you climb, you encounter narrow ridges, rocky cliffs, and occasional gusts of wind that try to sway you off course. Each step requires focus and determination, but the promise of reaching the mountaintop keeps you going.

Finally, after what feels like an arduous journey, you reach the summit. A sense of accomplishment washes over you as you take in the majestic panorama that unfolds before your eyes. Snow-capped peaks stretch as far as the eye can see, and a vast expanse of land lies beneath you.

The air is crisp and invigorating at this lofty height. You feel a profound sense of peace and awe as you stand at the pinnacle of the world, taking in the beauty and grandeur of nature's masterpiece.

In this moment, you realize that the true reward lies not only in reaching the mountaintop but also in the journey itself. The challenges you faced along the way have shaped you, pushing you to discover your inner strength and resilience.

As you stand atop the summit, you reflect on the lessons learned during your ascent. The mountain has taught you the value of perseverance, the beauty of embracing challenges, and the importance of setting ambitious goals.

Now, as you prepare to descend back to the world below, a gentle gust of wind whispers a final choice into your ear. You have the option to leave the mountaintop as it is, untouched and preserved in its natural splendor, or you can leave your mark upon it, building a small stone cairn as a tribute to your journey.

If you decide to leave the mountaintop untouched, enter 1.
If you choose to build a stone cairn as a tribute, enter 2.

Remember, this final choice will shape not only your connection to the mountain but also your legacy within its majestic embrace.''')
      choice4 = acceptAnswer(2)

      #LEVEL 4
      if choice4 == 1:
        print('''
        Feeling a deep reverence for the pristine beauty of the mountaintop and the wisdom it has imparted upon you, you choose to leave the summit untouched, preserving its natural splendor. You believe that by leaving it undisturbed, others can experience the same awe-inspiring views and profound sense of accomplishment that you have felt.

With a sense of gratitude and respect, you take a final moment to breathe in the crisp mountain air, imprinting the memory of this extraordinary journey into your heart. You step away from the summit, knowing that the mountain will continue to inspire and challenge those who dare to venture to its heights.

As you begin your descent, you carry the lessons and experiences of this journey with you. The mountain has become a part of you, a symbol of your determination, resilience, and connection to the natural world. Its wisdom will guide you in the chapters of your life that lie ahead.

With each step down the mountain, you reflect on the transformative power of nature and the mountains, grateful for the opportunity to have embarked on this remarkable adventure. You carry the memories of the summit, the challenges overcome, and the beauty witnessed, forever etched in your soul.

ENDING: A Legacy of Reverence''')
      #LEVEL 4
      elif choice4 == 2:
        print('''
        Feeling a deep connection to the mountaintop and a desire to leave a tangible mark of your journey, you decide to build a stone cairn as a tribute. With reverence and care, you search for stones of varying sizes, each one representing a step taken and a challenge overcome during your ascent.

As you carefully place each stone upon the mountaintop, a sense of purpose and gratitude fills your heart. The cairn begins to take shape, standing as a testament to your triumph over adversity and your bond with the mountain.

With each stone you add, you reflect on the lessons learned during your ascent — the strength of perseverance, the beauty of embracing challenges, and the importance of setting ambitious goals. Each rock symbolizes not just a physical accomplishment, but also a milestone in your personal growth.

As the cairn grows taller, it becomes a beacon of inspiration for future adventurers who will tread this path. It stands as a reminder that with determination and resilience, they too can conquer the challenges that lie ahead.

Completing the stone cairn, you step back to admire your creation. It stands proudly upon the mountaintop, a testament to your journey and a symbol of the human spirit's indomitable will. The wind whispers through the stones, carrying your story to the heavens and beyond.

With a sense of fulfillment, you begin your descent, knowing that your tribute will remain, silently witnessing the journeys of others who come to conquer the mountain. The stone cairn serves as a marker of your legacy, forever etching your presence into the mountain's history.

ENDING: The Cairn's Legacy''')
        
#LEVEL 1
elif choice1 == 2:
  print('''
  Leaving the forest behind, you embark on a journey to explore the surrounding countryside. You find yourself wandering through rolling hills, dotted with colorful wildflowers and grazing livestock. The warm rays of the sun bathe the landscape, creating a serene and peaceful ambiance.

As you traverse the countryside, you come across a fork in the road. One path leads towards a bustling village, where the sounds of laughter and music can be heard. The other path winds its way through a dense forest, similar to the one you decided not to enter earlier. The forest looks mysterious, but also a bit foreboding.

Now, it's time to make another decision. Which path will you choose to follow?

If you decide to head towards the bustling village, enter 1.
If you choose to venture into the dense forest, enter 2.

Remember, every path holds its own adventures and surprises. Trust your intuition, and let your journey unfold in the countryside outside "The Enchanted Forest."''')
  choice2 = acceptAnswer(2)

  #LEVEL 2
  if choice2 == 1:
    print('''
    Intrigued by the sounds of laughter and music drifting from the bustling village, you decide to follow the path that leads you in that direction. As you walk, the scenery changes from the tranquil countryside to a more vibrant and lively setting.

As you approach the village, you notice colorful banners fluttering in the breeze and the aroma of delicious food wafting through the air. The streets are lined with quaint cottages and bustling market stalls, offering an array of goods and wares.

The villagers greet you warmly, their faces filled with curiosity and friendliness. You find yourself drawn into their lively conversations, discovering tales of their traditions and festivities. The village square is abuzz with activity, with musicians playing lively tunes and dancers twirling to the rhythm.

Amidst the vibrant atmosphere, you spot a notice board filled with various announcements and requests. One catches your eye—a local merchant is seeking a brave adventurer to retrieve a valuable artifact from a nearby cavern. The reward is said to be great, but the cavern is rumored to be filled with challenges and dangers.

Now, it's time to make another decision. Will you take up the merchant's quest and venture into the treacherous cavern, or will you explore the village further and immerse yourself in its festivities?

If you decide to take up the merchant's quest, enter 1.
If you choose to immerse yourself in the village festivities, enter 2.

Remember, in "The Enchanted Forest," every choice you make shapes your unique adventure. Embrace the warmth of the village or embrace the call of adventure—it's up to you to decide your path.''')
    choice3 = acceptAnswer(2)
    
    #LEVEL 3
    if choice3 == 1:
      print('''
      Inspired by tales of adventure and the lure of new horizons, you decide to take up the merchant's quest. With a heart filled with anticipation, you set off on a journey to distant lands, eager to seek fortunes and weave your own story.

Equipped with a wagon full of wares and a map guiding you through treacherous terrains and bustling marketplaces, you traverse across vast landscapes and navigate through bustling cities. The road is not always smooth, but your determination and resourcefulness carry you forward.

Along the way, you encounter diverse cultures, forge new friendships, and learn the art of negotiation. Your skills as a merchant sharpen with each transaction, and your reputation spreads like wildfire. As you build connections and trade valuable goods, your wealth and influence grow.

Years pass, and you become a respected figure in the trading world, known for your integrity and shrewd business acumen. The merchant's quest has not only brought you riches but also bestowed upon you a profound understanding of the world and its myriad complexities.

As you reflect on your journey, you realize that wealth alone cannot satisfy the longing in your heart. The experiences and connections you've made are the true treasures of your voyage. The friendships and bonds forged along the way have enriched your life in ways you never imagined.

With a heart full of gratitude, you decide to retire from the bustling world of trade. You settle in a tranquil corner of the world, surrounded by the beauty of nature. Here, you find solace and contentment, knowing that you have left your mark on the merchant's path.

As you watch the sunset paint the sky with hues of gold and crimson, you reflect on the adventures, challenges, and triumphs that have shaped your journey. The merchant's quest has not only granted you material wealth but also a wealth of experiences, wisdom, and a legacy that will be remembered for generations to come.

In this peaceful haven, you spend your days sharing stories of your travels, passing down the knowledge and lessons you've gained to others who seek their own path. Your legacy as a merchant and adventurer lives on, inspiring a new generation to embark on their own quests, driven by curiosity and the desire to explore the unknown.

ENDING: The Merchant's Legacy''')
    #LEVEL 3
    elif choice3 == 2:
      print('''
      After a long and eventful journey, you find yourself drawn to the vibrant energy of a quaint village nestled amidst rolling hills and lush meadows. Intrigued by the simplicity and warmth of its inhabitants, you decide to immerse yourself in the activities of the village.

You awaken each day to the cheerful greetings of the villagers, who readily embrace you as one of their own. Eager to contribute, you lend a helping hand in the fields, tending to crops and nurturing the land that sustains the community. The earth beneath your fingertips and the scent of fresh soil invigorate your spirit, reminding you of the interconnectedness between nature and humanity.

As time passes, you become an integral part of the village's fabric, engaging in various communal activities. You join in lively festivals, dancing to traditional tunes that resonate through the streets. You participate in harvest celebrations, sharing in the joy of abundance and the fruits of collective labor. You listen to the elders' stories, absorbing their wisdom and preserving the oral history of the village.

Your skills and experiences from your travels prove invaluable to the community. You share tales of distant lands, introducing new perspectives and ideas. You teach the villagers innovative techniques and crafts, enabling them to expand their horizons and create unique works of art.

Over the years, you witness the village evolving and growing, nurtured by the collective efforts of its inhabitants. The once-small community now flourishes, enriched by a shared sense of purpose and unity.

As you reflect on your journey, you realize that immersing yourself in the village activities has brought a profound sense of fulfillment. The simplicity of life, the genuine connections forged, and the shared joys and sorrows have woven a tapestry of belonging and contentment within your heart.

In this village, you find a home, not only for your physical presence but also for your spirit. The laughter, the celebrations, and the support of the community have become an intrinsic part of your being.

As the years pass, you continue to contribute to the village, passing on the knowledge and skills you have acquired. Your presence leaves an indelible mark on the village's history, and your legacy lives on through the generations to come.

ENDING: The Village's heart''')
  #LEVEL 2
  elif choice2 == 2:
    print('''
    Intrigued by the mysteries hidden within the depths of the dense forest, you decide to venture into its embrace. The air grows cooler and the sunlight filters through the thick foliage, casting dappled patterns on the forest floor. Excitement and a sense of trepidation intertwine within you as you take your first steps into the unknown.

Navigating through the forest proves to be a challenge. The dense undergrowth and towering trees obscure your path, requiring careful observation and intuition to find your way. The silence is broken only by the rustling of leaves and the occasional calls of birds and woodland creatures.

As you delve deeper, you encounter a myriad of wonders. You stumble upon hidden waterfalls cascading into crystal-clear pools. You witness a kaleidoscope of colorful wildflowers blanketing the forest floor. You encounter rare and elusive creatures, their presence a testament to the untouched beauty of this enchanting realm.

The forest becomes your mentor, teaching you the art of patience and resilience. You learn to listen to the whispers of the wind, to read the patterns on the bark of ancient trees, and to follow the subtle signs left by the creatures that call this place home.

Days turn into weeks, and weeks into months as you lose yourself in the embrace of the forest. It becomes your sanctuary, a place where you find solace and inspiration. The forest nurtures your spirit, unveiling secrets and wisdom that can only be discovered through quiet observation and deep contemplation.

Along your journey, you encounter challenges that test your resolve. You face treacherous terrain and encounter mythical creatures guarding their sacred domains. Yet, with each obstacle overcome, you grow stronger and more attuned to the rhythms of the forest.

As you reach the heart of the forest, you discover a hidden grove, a sanctuary untouched by human hands. In this sacred space, you find a profound connection to nature and a deep understanding of the delicate balance that sustains all life.

In the depths of the forest, you find your purpose. Inspired by the wisdom and beauty surrounding you, you dedicate yourself to becoming its guardian and advocate, ensuring its preservation for generations to come. You become a steward of the forest, working alongside local communities and organizations to protect this precious ecosystem from the encroachment of civilization.

Your legacy is one of harmony and conservation. The forest becomes a symbol of your dedication and passion, a testament to the transformative power of nature and the profound connection between humanity and the natural world.

ENDING: The Forest's Guardian''')

        
  