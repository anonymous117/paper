
if __name__ == "__main__":

    filename = "cost"
    f = open(filename, "r")
    values = []
    ps = []
    for x in f:
        line = x
        # parse value
        v = line
        pos = v.find(",")
        v = v[:pos]
        value = float(v)
        #print(value)
        values.append(value)
        # parse p
        p = line
        pos = p.find(",")
        pos += 1
        p = p[pos:]
        processes = float(p)
        #print(processes)
        ps.append(processes)
    f.close()

    #print(values)
    #print(ps)

    max_cost = 43872980.46561268

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

    f = open(filename+"_result", "w")
    dict = {'max cost': max_cost, 'total cost': total_cost, 'percent cost': percent}
    f.write( 'dict = ' + repr(dict) + '\n' )
    f.close()
