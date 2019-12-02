
if __name__ == "__main__":
    f = open("cost", "r")
    values = []
    ps = []
    for x in f:
        line = x
        # parse value
        v = line
        pos = v.find("=")
        pos += 2
        v = v[pos:]
        value = float(v)
        values.append(value)
        # parse p
        p = line
        pos = p.find("p")
        pos += 2
        p = p[pos:]
        pos = p.find(")")
        p = p[:pos]
        processes = float(p)
        ps.append(processes)
    f.close()

    #print(values)
    #print(ps)

    max_cost = 9801124.1712

    total_cost = 0
    for i in range(len(values)):
        point_cost = ps[i] * values[i]
        print("point "+str(i)+" cost: "+str(point_cost))
        total_cost += point_cost

    print("\nfull matrix cost:",max_cost)    
    print("used point cost:",total_cost)

    # calc percentage used point costs
    one_percent = max_cost / 100
    percent = total_cost / one_percent

    print("percent used point cost:",percent)

    f = open("cost_result", "w")
    dict = {'max cost': max_cost, 'total cost': total_cost, 'percent cost': percent}
    f.write( 'dict = ' + repr(dict) + '\n' )
    f.close()