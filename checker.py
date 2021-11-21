import math
import sys

def utf8text(maybe_bytes, errors='strict'):
  if maybe_bytes is None:
    return None
  if isinstance(maybe_bytes, str):
    return maybe_bytes
  return maybe_bytes.decode('utf-8', errors)

def getNorm(n, x, L):
  ret = 0
  for i in range(n):
    for j in L[i]:
      ret += L[i][j] * ((y[j] - y[i]) ** 2)
  return ret ** 0.5

def check(process_output, case_output, case_input):
  process_lines = utf8text(process_output).split('\n')
  output_lines = utf8text(case_output).split('\n')
  input_lines = utf8text(case_input).split('\n')

  n, _, m = map(int, input_lines[0].split())

  barx = [float(x) for x in output_lines]
  try:
    x = [float(z) for z in process_lines]
  except:
    print(f'could not parse x', file=sys.stderr)
    return 1

  if len(x) != n:
    print(f'expected {n} entries, got {len(x)} instead')
    return 1
  if any(math.isnan, x):
    print('Nan detected')
    return 1

  # compute L
  L = [{} for _ in range(n)]
  for edge in input_lines[1:]:
    u, v, w = edge.split()
    u = int(u) - 1
    v = int(v) - 1
    w = float(w)
    L[u][v] = L[v][u] = w

  xDiff = [x[i] - barx[i] for i in range(n)]
  xDiffNorm = getNorm(n, barx, L)
  xNorm = getNorm(n, barx, L)
  print(f'xNorm = {xNorm:.3g}, diff = {xDiffNorm:.3g}, ratio = {xDiffNorm/xNorm:.10g}')
  return 0

if __name__ == '__main__':
  sys.exit(check(sys.argv[1], sys.argv[2], sys.argv[3]))
