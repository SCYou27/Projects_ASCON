using CLSCA
using NPZ

quicklimit  = 0 # 2^10 had no speed benefit
searchlimit = 2^24

for run = parse.(Int, ARGS)
    if run == 1
        experiment = "U-Os";
        frag = "direct"
        traces = string.(1:10; pad=2)
    elseif run == 2
        experiment = "U-Os";
        frag = "bytes"
        traces = string.(1:10; pad=2)
    elseif run == 3
        experiment = "U-Os";
        frag = "16bits"
        traces = string.(1:10; pad=2)
    elseif run == 4
        experiment = "U-Os";
        frag = "bits"
        traces = string.(1:10; pad=2)
    elseif run == 5
        experiment = "U-O3";
        frag = "direct"
        traces = string.(1:10; pad=2)
    elseif run == 6
        experiment = "U-O3";
        frag = "bytes"
        traces = string.(1:10; pad=2)
    elseif run == 7
        experiment = "U-O3";
        frag = "16bits"
        traces = string.(1:10; pad=2)
    elseif run == 8
        experiment = "U-O3";
        frag = "bits"
        traces = string.(1:10; pad=2)
    elseif run == 9
        experiment = "M-Os";
        frag = "direct_O"
        traces = string.([1:10; 20; 50; 100]; pad=4)
    elseif run == 10
        experiment = "M-Os";
        frag = "bytes_O"
        traces = string.([1:10; 20; 50; 100]; pad=4)
    elseif run == 11
        experiment = "M-Os";
        frag = "direct_S"
        traces = string.([1:10; 20; 50; 100]; pad=4)
    elseif run == 12
        experiment = "M-Os";
        frag = "bytes_S"
        traces = string.([1:10; 20; 50; 100]; pad=4)
    else
        @error "what?"
    end

    if frag == "16bits";
        F = UInt16
    elseif frag == "bits";
        F = UInt8
    elseif frag == "bytes";
        F = UInt8
    elseif frag == "bytes_O";
        F = UInt8
    elseif frag == "bytes_S";
        F = UInt8
    elseif frag == "direct";
        F = UInt8
    elseif frag == "direct_O";
        F = UInt8
    elseif frag == "direct_S";
        F = UInt8
    else
        @error "what?"
    end

    # iterate over keys 0000 to 0999
    keys = 1000
    result = Array{Float64,3}(undef, keys, length(traces), 5)
    println(Threads.nthreads(), " threads")
    Threads.@threads for n = 0:(keys-1)
        n4 = string(n; pad=4)
        k = F.(npzread("$experiment/Key_$frag/key_$n4.npy"))
        # iterate over number of traces L01 to L09
        for L = eachindex(traces)
            L2 = traces[L]
            t = npzread("$experiment/Tables_$frag/L$L2/table_$n4.npy")
            p = t[:,:,2]'
            v = F.(t[:,:,1]')
            r = nothing
            if quicklimit > 0
                # first do an initial enumeration
                e = KeyEnumerator(p,v)
                r = depth(e, k, quicklimit)
            end
            if r === nothing
                # then do a histogram-based estimate
                est, low, high = estimate_rank(p,v,k, H=Float64)
                if low <= searchlimit
                    e = KeyEnumerator(p,v)
                    r = depth(e, k, min(high, searchlimit))
                    if r === nothing
                        d = -1   # not found
                        prob = -1
                    else
                        (d, prob) = r
                    end
                else
                    d = -2  # not searched
                end
            else
                # the quick initial enumeration already found it
                (d, prob) = r
                low = -1
                est = -1
                high = -1
            end
            println("$experiment/Tables_$frag/L$L2/$n4: $low <= $est ~ $d <= $high")
            best = est
            if d >= 0; best = d; end
            result[n+1, L, :] = [best, low, est, d, high]
        end
    end
    npzwrite("$experiment-Tables_$frag-result.npy", result)
end
