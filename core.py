def truncate(seq: str, length: int, method: str = 'rhs') -> str:
    seq_len = len(seq)
    if seq_len <= length:
        return seq
    else:
        if method == 'rhs':
            length -= 4
            return f'{seq[:length]} ...'
        elif method == 'lhs':
            length -= 4
            return f'... {seq[-length:]}'
        elif method == 'middle':
            left = right = (length - 5) // 2
            if left + right + 5 < length:
                left += 1
            return f'{seq[:left]} ... {seq[-right:]}'
        else:
            msg = f'method should be either lhs, middle or rhs'
            raise ValueError(msg)
