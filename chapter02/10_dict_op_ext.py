# dict μπορούμε να έχουμε με πολλούς διάφορους τύπους
sym = {
  "key1": "value1",
  "key2": 10,
  3: [100, 200, 300],
  4: {1: "one", 2: "two"},
  (1, 2): 1,
  frozenset({1, 2}): "set" # τώρα γίνεται immutable και περνάει σαν key
  # {1, 2}: "set" # αυτό δεν γίνεται γιατί τα keys πρέπει να είναι hashable (immutable)
  # [1, 2]: 10 # αυτό δεν γίνεται γιατί τα keys πρέπει να είναι hashable (immutable)
}
print(sym)